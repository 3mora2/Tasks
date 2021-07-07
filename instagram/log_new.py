import json, warnings
import random
import re
from io import BytesIO
from datetime import datetime
import gzip
from socket import timeout, error as SocketError
from ssl import SSLError
import hmac
import hashlib
import uuid
import urllib.parse as compat_urllib_parse
from urllib.parse import urlparse as compat_urllib_parse_urlparse
import http.client as compat_http_client
import http.cookiejar as compat_cookiejar
import urllib.error as compat_urllib_error
import urllib.request as compat_urllib_request
import pickle as compat_pickle

import time
import logging

logger = logging.getLogger(__name__)

import requests


def Get_Id(url):
    url += '?__a=1'
    r = requests.get(url)
    try:
        data = json.loads(r.text)
        if '/p/' in url:
            return data['graphql']['shortcode_media']['id']
        else:
            return data['graphql']['user']['id']
    except (json.decoder.JSONDecodeError, KeyError):
        return None


VALID_UUID_RE = r'^[a-f\d]{8}\-[a-f\d]{4}\-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}$'


def raise_if_invalid_rank_token(val, required=True):
    if required and not val:
        raise ValueError('rank_token is required')
    if not re.match(VALID_UUID_RE, val):
        raise ValueError('Invalid rank_token: {}'.format(val))


class ClientCookieJar(compat_cookiejar.CookieJar):
    """Custom CookieJar that can be pickled to/from strings
    """

    def __init__(self, cookie_string=None, policy=None):
        compat_cookiejar.CookieJar.__init__(self, policy)
        if cookie_string:
            if isinstance(cookie_string, bytes):
                self._cookies = compat_pickle.loads(cookie_string)
            else:
                self._cookies = compat_pickle.loads(cookie_string.encode('utf-8'))

    @property
    def auth_expires(self):
        for cookie in self:
            if cookie.name in ('ds_user_id', 'ds_user'):
                return cookie.expires
        return None

    @property
    def expires_earliest(self):
        """For backward compatibility"""
        return self.auth_expires

    def dump(self):
        return compat_pickle.dumps(self._cookies)


class ClientDeprecationWarning(DeprecationWarning):
    pass


class ClientPendingDeprecationWarning(PendingDeprecationWarning):
    pass


class ClientExperimentalWarning(UserWarning):
    pass


class MediaTypes(object):
    """Psuedo enum-ish/lookup class for media types."""

    PHOTO = 1  #: Photo type
    VIDEO = 2  #: Video type
    CAROUSEL = 8  #: Carousel/Album type

    ALL = (PHOTO, VIDEO, CAROUSEL)

    __media_type_map = {
        'image': PHOTO,
        'video': VIDEO,
        'carousel': CAROUSEL,
    }

    @staticmethod
    def id_to_name(media_type_id):
        """Convert a media type ID to its name"""
        try:
            return [k for k, v in MediaTypes.__media_type_map.items() if v == media_type_id][0]
        except IndexError:
            raise ValueError('Invalid media ID')

    @staticmethod
    def name_to_id(media_type_name):
        """Convert a media type name to its ID"""
        try:
            return MediaTypes.__media_type_map[media_type_name]
        except KeyError:
            raise ValueError('Invalid media name')


class ClientCompatPatch(object):
    """Utility to make entities from the private api similar to the ones
    from the public one by adding the necessary properties, and if required,
    remove any incompatible properties (to save storage space for example).
    """
    FILTERS = {
        -2: 'OES',
        -1: 'YUV',
        0: 'Normal',
        1: 'X-Pro II',
        2: 'Lo-Fi',
        3: 'Earlybird',
        10: 'Inkwell',
        14: '1977',
        15: 'Nashville',
        16: 'Kelvin',
        17: 'Mayfair',
        18: 'Sutro',
        19: 'Toaster',
        20: 'Walden',
        21: 'Hefe',
        22: 'Brannan',
        23: 'Rise',
        24: 'Amaro',
        25: 'Valencia',
        26: 'Hudson',
        27: 'Sierra',
        28: 'Willow',
        105: 'Dogpatch',
        106: 'Vesper',
        107: 'Ginza',
        108: 'Charmes',
        109: 'Stinson',
        111: 'Moon',
        112: 'Clarendon',
        113: 'Skyline',
        114: 'Gingham',
        115: 'Brooklyn',
        116: 'Ashby',
        117: 'Helena',
        118: 'Maven',
        603: 'Ludwig',
        605: 'Slumber',
        608: 'Perpetua',
        612: 'Aden',
        613: 'Juno',
        614: 'Reyes',
        615: 'Lark',
        616: 'Crema',
        640: 'BrightContrast',
        642: 'CrazyColor',
        643: 'SubtleColor',
    }

    @staticmethod
    def _get_closest_size(medias, width, height=0):
        """
        Try to extract a image/video object that will most match the resolution returned by the public API

        :param medias: list of images/videos
        :param width: desired width
        :param height: desired height
        :return:
        """
        current = None
        for media in medias:
            if not current:
                current = media
            if (abs(media['width'] - width) < abs(current['width'] - width) or
                    (media['width'] == current['width'] and not height and
                     not media['height'] == current['width']) or
                    (media['width'] == current['width'] and height and
                     abs(media['height'] - height) < abs(current['height'] - height))):
                current = media

        return current

    @staticmethod
    def _drop_keys(obj, keys):
        """
        Drop unwanted dict keys

        :param obj:
        :param keys:
        :return:
        """
        for k in keys:
            obj.pop(k, None)

    @classmethod
    def comment(cls, comment, drop_incompat_keys=False):
        """Patch a comment object"""
        comment['created_time'] = str(int(comment.get('created_at')))
        from_user = {
            'username': comment['user']['username'],
            'profile_picture': comment['user']['profile_pic_url'],
            'id': str(comment['user']['pk']),
            'full_name': comment['user']['full_name'],
        }
        comment['from'] = from_user
        comment['id'] = str(comment['pk'])
        if drop_incompat_keys:
            cls._drop_keys(
                comment,
                [
                    'bit_flags',
                    'content_type',
                    'created_at',
                    'created_at_utc',
                    'media_id',
                    'pk',
                    'status',
                    'type',
                    'user',
                    'user_id',
                ]
            )
        return comment

    @classmethod
    def media(cls, media, drop_incompat_keys=False):
        """Patch a media object"""
        media['link'] = 'https://www.instagram.com/p/{0!s}/'.format(media['code'])
        media['created_time'] = str(int(media.get('taken_at') or media.get('device_timestamp')))

        if media['media_type'] == MediaTypes.PHOTO:
            media['type'] = 'image'
        elif media['media_type'] == MediaTypes.VIDEO:
            media['type'] = 'video'
        elif media['media_type'] == MediaTypes.CAROUSEL:
            media['type'] = 'carousel'  # will be patched over below

        if media['caption']:
            media['caption']['id'] = str(media['caption']['pk'])
            media['caption']['created_time'] = str(int(media['caption']['created_at']))
            caption_from = {
                'username': media['caption']['user']['username'],
                'profile_picture': media['caption']['user']['profile_pic_url'],
                'id': str(media['caption']['user']['pk']),
                'full_name': media['caption']['user']['full_name'],
            }
            media['caption']['from'] = caption_from
            if drop_incompat_keys:
                cls._drop_keys(
                    media['caption'],
                    [
                        'bit_flags',
                        'content_type',
                        'created_at',
                        'created_at_utc',
                        'has_translation',
                        'media_id',
                        'pk',
                        'status',
                        'type',
                        'user',
                    ]
                )
        media['user'] = cls.list_user(media['user'], drop_incompat_keys=drop_incompat_keys)
        if media['media_type'] == MediaTypes.CAROUSEL and media.get('carousel_media', []):
            # patch carousel media
            for carousel_media in media.get('carousel_media', []):
                if carousel_media['media_type'] == MediaTypes.PHOTO:
                    carousel_media['type'] = 'image'
                elif carousel_media['media_type'] == MediaTypes.VIDEO:
                    carousel_media['type'] = 'video'
                image_versions2 = carousel_media.get('image_versions2', {}).get('candidates', [])
                images = {
                    'low_resolution': cls._get_closest_size(image_versions2, 320),
                    'thumbnail': cls._get_closest_size(image_versions2, 150, 150),
                    'standard_resolution': cls._get_closest_size(
                        image_versions2, carousel_media.get('original_width', 1000)),
                }
                carousel_media['images'] = images
                if carousel_media['media_type'] == MediaTypes.VIDEO:
                    video_versions = carousel_media.get('video_versions', [])
                    videos = {
                        'low_bandwidth': cls._get_closest_size(video_versions, 480),
                        'standard_resolution': cls._get_closest_size(
                            video_versions, carousel_media.get('original_width', 640)),
                        'low_resolution': cls._get_closest_size(video_versions, 640),
                    }
                    if drop_incompat_keys:
                        [cls._drop_keys(i, ['type']) for i in list(videos.values())]
                    carousel_media['videos'] = videos

                # patch user tags
                if carousel_media.get('usertags', {}).get('in', []):
                    usertags = carousel_media['usertags']['in']
                    user_tags = []
                    for ut in usertags:
                        pos = {'y': ut['position'][1], 'x': ut['position'][0]}
                        user = ut['user']
                        user['id'] = str(ut['user']['pk'])
                        user['profile_picture'] = ut['user']['profile_pic_url']
                        if drop_incompat_keys:
                            cls._drop_keys(user, ['profile_pic_url', 'pk', 'is_private'])

                        user_tags.append({
                            'position': pos,
                            'user': user,
                        })
                    carousel_media['users_in_photo'] = user_tags
                # patch location
                if 'location' not in carousel_media or not carousel_media['location'].get('lat'):
                    carousel_media['location'] = None
                else:
                    carousel_media['location']['latitude'] = carousel_media['location']['lat']
                    carousel_media['location']['longitude'] = carousel_media['location']['lng']
                    carousel_media['location']['id'] = carousel_media['location']['pk']

            first_carousel_media = media['carousel_media'][0]
            media['images'] = first_carousel_media['images']
            media['type'] = first_carousel_media['type']
            if first_carousel_media['media_type'] == MediaTypes.VIDEO:
                media['videos'] = first_carousel_media['videos']
        else:
            image_versions2 = media.get('image_versions2', {}).get('candidates', [])
            images = {
                'low_resolution': cls._get_closest_size(image_versions2, 320),
                'thumbnail': cls._get_closest_size(image_versions2, 150, 150),
                'standard_resolution': cls._get_closest_size(image_versions2, media.get('original_width', 1000)),
            }
            media['images'] = images

        if media['media_type'] == MediaTypes.VIDEO:
            video_versions = media.get('video_versions', [])
            videos = {
                'low_bandwidth': cls._get_closest_size(video_versions, 480),
                'standard_resolution': cls._get_closest_size(video_versions, media.get('original_width', 640)),
                'low_resolution': cls._get_closest_size(video_versions, 640),
            }
            if drop_incompat_keys:
                [cls._drop_keys(i, ['type']) for i in list(videos.values())]
            media['videos'] = videos

        likes = {
            'count': media.get('like_count', 0),
            'data': []
        }
        media['likes'] = likes
        comments = {
            'count': media.get('comment_count', 0),
            # Patch comment too
            'data': [
                cls.comment(c, drop_incompat_keys=drop_incompat_keys)
                for c in media.get('comments', [])
            ]
        }
        media['comments'] = comments
        if media.get('preview_comments'):
            [
                cls.comment(c, drop_incompat_keys=drop_incompat_keys)
                for c in media.get('preview_comments', [])
            ]

        media['attribution'] = None
        if media.get('filter_type') is not None and media.get('filter_type') in cls.FILTERS:
            media['filter'] = cls.FILTERS[media.get('filter_type')]
        else:
            media['filter'] = ''
        media['user_has_liked'] = media.get('has_liked', False)

        # Try to preserve location even if there's no lat/lng/pk
        if 'location' not in media or not media['location']:
            media['location'] = None
        elif (media.get('location', {}).get('lat')
              and media.get('location', {}).get('lng')
              and media.get('location', {}).get('pk')):
            media['location']['latitude'] = media['location']['lat']
            media['location']['longitude'] = media['location']['lng']
            media['location']['id'] = media['location']['pk']
        # For stories
        if (not media.get('location')
                and media.get('story_locations')
                and media.get('story_locations', [{}])[0].get('location')):
            story_location = media['story_locations'][0]['location']
            if (story_location.get('lat')
                    and story_location.get('lng')
                    and story_location.get('pk')):
                media['location'] = story_location

        media['tags'] = []
        if media.get('usertags', {}).get('in', []):
            usertags = media['usertags']['in']
            user_tags = []
            for ut in usertags:
                pos = {'y': ut['position'][1], 'x': ut['position'][0]}
                user = ut['user']
                user['id'] = str(ut['user']['pk'])
                user['profile_picture'] = ut['user']['profile_pic_url']
                if drop_incompat_keys:
                    cls._drop_keys(user, ['profile_pic_url', 'pk', 'is_private'])

                user_tags.append({
                    'position': pos,
                    'user': user,
                })
            media['users_in_photo'] = user_tags
        elif media.get('reel_mentions'):
            reel_mentions = media['reel_mentions']
            user_tags = []
            for rm in reel_mentions:
                pos = {'y': rm['y'], 'x': rm['x']}
                user = rm['user']
                user['id'] = str(rm['user']['pk'])
                user['profile_picture'] = rm['user']['profile_pic_url']
                if drop_incompat_keys:
                    cls._drop_keys(user, ['profile_pic_id', 'profile_pic_url', 'pk', 'is_private'])
                user_tags.append({
                    'position': pos,
                    'user': user,
                })
            media['users_in_photo'] = user_tags
        else:
            media['users_in_photo'] = []

        if drop_incompat_keys:
            cls._drop_keys(
                media,
                [
                    'can_viewer_save',
                    'caption_is_edited',
                    'client_cache_key',
                    'code',
                    'comment_count',
                    'comments_disabled',
                    'comment_likes_enabled',
                    'device_timestamp',
                    'filter_type',
                    'has_audio',
                    'has_liked',
                    'has_more_comments',
                    'image_versions2',
                    'is_reel_media',
                    'lat',
                    'like_count',
                    'lng',
                    'max_num_visible_preview_comments',
                    'media_type',
                    'next_max_id',
                    'organic_tracking_token',
                    'original_height',
                    'original_width',
                    'photo_of_you',
                    'pk',
                    'preview_comments',
                    'reel_mentions',
                    'saved_collection_ids',
                    'taken_at',
                    'top_likers',
                    'video_duration',
                    'video_versions',
                    'view_count',
                    'visibility',
                ]
            )
            if media['location']:
                cls._drop_keys(
                    media['location'],
                    [
                        'address',
                        'city',
                        'external_id',
                        'external_source',
                        'facebook_places_id',
                        'foursquare_v2_id',
                        'lat',
                        'lng',
                        'pk',
                        'state',
                    ]
                )
        return media

    @classmethod
    def user(cls, user, drop_incompat_keys=False):
        """Patch a user object """
        user['id'] = str(user['pk'])
        user['bio'] = user.get('biography', '')
        user['profile_picture'] = user['profile_pic_url']
        user['website'] = user.get('external_url', '')
        if 'media_count' in user and 'follower_count' in user and 'following_count' in user:
            counts = {
                'media': user['media_count'],
                'followed_by': user['follower_count'],
                'follows': user['following_count']
            }
            user['counts'] = counts
        if drop_incompat_keys:
            cls._drop_keys(
                user,
                [
                    'auto_expand_chaining',
                    'biography',
                    'external_lynx_url',
                    'external_url',
                    'follower_count',
                    'following_count',
                    'geo_media_count',
                    'has_anonymous_profile_picture',
                    'has_chaining',
                    'hd_profile_pic_url_info',
                    'hd_profile_pic_versions',
                    'include_direct_blacklist_status',
                    'is_business',
                    'is_favorite',
                    'is_private',
                    'is_unpublished',
                    'is_verified',
                    'media_count',
                    'pk',
                    'profile_context',
                    'profile_pic_id',
                    'profile_pic_url',
                    'usertags_count',
                ]
            )
        return user

    @classmethod
    def list_user(cls, user, drop_incompat_keys=False):
        """
        Patch a list user object, example in
        :meth:`Client.user_following`, :meth:`Client.user_followers`, :meth:`Client.search_users`
        """
        user['id'] = str(user['pk'])
        user['profile_picture'] = user['profile_pic_url']
        if drop_incompat_keys:
            cls._drop_keys(
                user,
                [
                    'byline',
                    'follower_count',
                    'friendship_status',
                    'has_anonymous_profile_picture',
                    'has_chaining',
                    'is_favorite',
                    'is_private',
                    'is_unpublished',
                    'is_verified',
                    'mutual_followers_count',
                    'pk',
                    'profile_pic_url',
                    'social_context',
                    'unseen_count',
                ]
            )
        return user


class Constants(object):
    """Constants holder class that stores the bulk of the fixed strings used in the library."""

    IG_SIG_KEY = '19ce5f445dbfd9d29c59dc2a78c616a7fc090a8e018b9267bc4240a30244c53b'
    IG_CAPABILITIES = '3brTvw=='
    SIG_KEY_VERSION = '4'
    APP_VERSION = '76.0.0.15.395'
    APPLICATION_ID = '567067343352427'
    FB_HTTP_ENGINE = 'Liger'

    ANDROID_VERSION = 24
    ANDROID_RELEASE = '7.0'
    PHONE_MANUFACTURER = 'samsung'
    PHONE_DEVICE = 'SM-G930F'
    PHONE_MODEL = 'herolte'
    PHONE_DPI = '640dpi'
    PHONE_RESOLUTION = '1440x2560'
    PHONE_CHIPSET = 'samsungexynos8890'
    VERSION_CODE = '138226743'

    USER_AGENT_FORMAT = \
        'Instagram {app_version} Android ({android_version:d}/{android_release}; ' \
        '{dpi}; {resolution}; {brand}; {device}; {model}; {chipset}; en_US; {version_code})'

    USER_AGENT_EXPRESSION = \
        r'Instagram\s(?P<app_version>[^\s]+)\sAndroid\s\((?P<android_version>[0-9]+)/(?P<android_release>[0-9\.]+);\s' \
        r'(?P<dpi>\d+dpi);\s(?P<resolution>\d+x\d+);\s(?P<manufacturer>[^;]+);\s(?P<device>[^;]+);\s' \
        r'(?P<model>[^;]+);\s(?P<chipset>[^;]+);\s[a-z]+_[A-Z]+;\s(?P<version_code>\d+)'

    USER_AGENT = USER_AGENT_FORMAT.format(**{
        'app_version': APP_VERSION,
        'android_version': ANDROID_VERSION,
        'android_release': ANDROID_RELEASE,
        'brand': PHONE_MANUFACTURER,
        'device': PHONE_DEVICE,
        'model': PHONE_MODEL,
        'dpi': PHONE_DPI,
        'resolution': PHONE_RESOLUTION,
        'chipset': PHONE_CHIPSET,
        'version_code': VERSION_CODE})

    LOGIN_EXPERIMENTS = 'ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_android_icon_perf2,ig_android_autosubmit_password_recovery_universe,ig_android_background_voice_phone_confirmation_prefilled_phone_number_only,ig_android_report_nux_completed_device,ig_account_recovery_via_whatsapp_universe,ig_android_stories_reels_tray_media_count_check,ig_android_background_voice_confirmation_block_argentinian_numbers,ig_android_device_verification_fb_signup,ig_android_reg_nux_headers_cleanup_universe,ig_android_reg_omnibox,ig_android_background_voice_phone_confirmation,ig_android_gmail_autocomplete_account_over_one_tap,ig_android_phone_reg_redesign_universe,ig_android_skip_signup_from_one_tap_if_no_fb_sso,ig_android_reg_login_profile_photo_universe,ig_android_access_flow_prefill,ig_android_email_suggestions_universe,ig_android_contact_import_placement_universe,ig_android_ask_for_permissions_on_reg,ig_android_onboarding_skip_fb_connect,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_account_switch_infra_universe,ig_android_hide_fb_connect_for_signup,ig_restore_focus_on_reg_textbox_universe,ig_android_login_identifier_fuzzy_match,ig_android_suma_biz_account,ig_android_session_scoping_facebook_account,ig_android_security_intent_switchoff,ig_android_do_not_show_back_button_in_nux_user_list,ig_android_aymh_signal_collecting_kill_switch,ig_android_nux_add_email_device,ig_android_multi_tap_login_new,ig_android_persistent_duplicate_notif_checker,ig_android_login_safetynet,ig_android_fci_onboarding_friend_search,ig_android_editable_username_in_reg,ig_android_phone_auto_login_during_reg,ig_android_one_tap_fallback_auto_login,ig_android_device_detection_info_upload,ig_android_updated_copy_user_lookup_failed,ig_fb_invite_entry_points,ig_android_hsite_prefill_new_carrier,ig_android_gmail_oauth_in_reg,ig_two_fac_login_screen,ig_android_reg_modularization_universe,ig_android_passwordless_auth,ig_android_sim_info_upload,ig_android_universe_noticiation_channels,ig_android_realtime_manager_cleanup_universe,ig_android_analytics_accessibility_event,ig_android_direct_main_tab_universe,ig_android_email_one_tap_auto_login_during_reg,ig_android_prefill_full_name_from_fb,ig_android_directapp_camera_open_and_reset_universe,ig_challenge_kill_switch,ig_android_video_bug_report_universe,ig_account_recovery_with_code_android_universe,ig_prioritize_user_input_on_switch_to_signup,ig_android_modularized_nux_universe_device,ig_android_account_recovery_auto_login,ig_android_hide_typeahead_for_logged_users,ig_android_targeted_one_tap_upsell_universe,ig_android_caption_typeahead_fix_on_o_universe,ig_android_retry_create_account_universe,ig_android_crosshare_feed_post,ig_android_abandoned_reg_flow,ig_android_remember_password_at_login,ig_android_smartlock_hints_universe,ig_android_2fac_auto_fill_sms_universe,ig_type_ahead_recover_account,ig_android_onetaplogin_optimization,ig_android_family_apps_user_values_provider_universe,ig_android_smart_prefill_killswitch,ig_android_direct_inbox_account_switching,ig_android_exoplayer_settings,ig_android_bottom_sheet,ig_android_publisher_integration,ig_sem_resurrection_logging,ig_android_login_forgot_password_universe,ig_android_hindi,ig_android_hide_fb_flow_in_add_account_flow,ig_android_dialog_email_reg_error_universe,ig_android_low_priority_notifications_universe,ig_android_device_sms_retriever_plugin_universe,ig_android_device_verification_separate_endpoint'  # noqa

    EXPERIMENTS = 'ig_camera_android_badge_face_effects_universe,ig_android_dash_lazy_load_audio,ig_android_stories_landscape_mode,ig_android_whitehat_options_universe,ig_android_fb_profile_integration_fbnc_universe,ig_android_vc_create_thread_upon_call_initiation_universe,ig_android_stories_seen_state_swipe_forward_universe,ig_android_realtime_mqtt_logging,ig_branded_content_show_settings_universe,ig_android_stories_server_coverframe,ig_android_direct_mutation_manager_handler_thread_universe,ig_android_ad_async_ads_universe,ig_android_camera_arengine_shader_caching_universe,ig_android_live_audiomanager_leak,ig_feed_lockdown,ig_android_interactions_preview_comment_impression_universe,ig_android_enable_igrtc_module,ig_android_direct_vm_activity_sheet,ig_android_appstate_logger,ig_android_direct_breeze_sheet,ig_android_camera_new_post_smile_universe,ig_android_live_video_position_source_universe,mi_viewpoint_feed_switchover,ig_feed_ranking_report_issue,ig_camera_android_areffect_photo_capture_universe,ig_rtc_use_dtls_srtp,ig_android_video_prefetch_feed_fix,ig_android_direct_remove_in_composer_camera_button_animation_universe,ig_android_live_fault_tolerance_universe,ig_android_igtv_autoplay_on_prepare,ig_android_main_feed_new_posts_indicator_universe,ig_android_audience_control,ig_android_stories_gif_upload_fix,ig_android_one_tap_fbshare,ig_android_startup_thread_priority,ig_android_stories_question_sticker_new_formats_universe,ig_android_business_transaction_in_stories_consumer,ig_android_search_impression_logging,ig_android_rtl_api28_textlayout_crash_universe,ig_android_direct_thread_sidebar_send_states,ig_fbns_push,ig_face_effect_ranking,ig_android_direct_albums,ig_search_null_state_universe,ig_android_stories_music_sticker_default_variation,ig_android_direct_update_thread_metadata_universe,ig_android_codec_high_profile,ig_android_inline_appeal,ig_rti_inapp_notifications_universe,ig_promote_last_used_destination_universe,ig_android_vc_directapp_integration_universe,allow_publish_page_universe,ig_android_maintabfragment,ig_android_skip_get_fbupload_universe,ig_android_low_data_mode,ig_android_enable_zero_rating,ig_android_main_feed_refresh_style_universe,ig_android_reverse_audio,ig_background_prefetch,ig_android_request_verification_badge,ig_android_http_stack_experiment_2017,ig_direct_android_24h_visual_perf,ig_android_live_thread_delay_for_mute_universe,ig_android_fb_topsearch_sgp_fork_request,ig_hashtag_display_universe,ig_android_banyan_migration,ig_android_heap_uploads,ig_android_cookie_serialization_optimization_universe,ig_android_mqtt_cookie_auth_memcache_universe,ig_android_stories_feeback_message_composer_entry_point,ig_android_instacrash_detection,ig_explore_2018_h2_account_rec_deduplication_android,ig_android_photo_hashing,ig_android_increase_fd_limit,ig_android_log_failed_image_download_retries,ig_android_live_use_timestamp_normalizer,ig_android_direct_async_thread_store,ig_android_persistent_nux,ig_android_story_accidentally_click_investigation_universe,ig_android_live_capture_translucent_navigation_bar,ig_android_churned_find_friends_redirect_to_discover_people,ig_android_vc_capture_universe,ig_android_story_reactions,ig_android_video_playback_retry_time_threshold,ig_android_mi_netego_long_event_removal_universe,ig_android_global_scheduler_infra,ig_end_of_feed_ranking_universe,ig_android_live_emoji_easter_egg_universe,ig_stories_in_feed_unit_design_universe,ig_android_ads_manager_pause_resume_ads_universe,ig_android_show_welcome_card_self_post_universe,ig_android_hashtag_header_display,ig_android_delay_coldstart_logging,ig_android_explore_grid_icon_removal_universe,ig_android_hashtag_contextual_feed_follow_button,ig_internal_research_settings,ig_smb_ads_basket_of_values_universe,ig_android_shopping_pdp_universe,ig_android_anr,ig_close_friends_v4,ig_android_feed_seen_state_with_view_info,ig_android_direct_visual_previews_in_thread,ig_promote_budget_warning_view_universe,ig_android_vc_camera_zoom_universe,ig_promote_daily_budget_multiplier_universe,ig_android_interactions_direct_share_comment_universe,ig_camera_android_supported_capabilities_api_universe,ig_android_post_recs_hide_from_author_universe,ig_android_biz_conversion_editable_profile_review_universe,ig_android_ad_increase_story_adpreload_priority_universe,ig_android_cache_video_autoplay_checker,ig_android_photo_fbuploader_config,ig_android_ad_watchlead_universe,ig_android_live_viewer_single_tap_invite_universe,ig_android_cold_start_json_delivery_improvement,ig_stories_suggestions_for_small_tray_universe,ig_shopping_catalog_selection_done_button,ig_inventory_connections,ig_android_fb_profile_integration_universe,ig_android_stories_weblink_creation,ig_android_live_start_broadcast_optimized_universe,ig_android_netgo_cta,ig_android_histogram_reporter,ig_android_vc_universe,ig_fb_graph_differentiation_no_fb_data,ig_android_network_cancellation,ig_android_live_presence_universe,ig_android_search_normalization_recipients,ig_android_connect_owned_page_universe,ig_android_downloaded_image_decode_universe,ig_android_realtime_stories_fetching,ig_android_hashtag_following,ig_android_felix_release_all_players_on_pause,ig_android_low_data_mode_backup_1,ig_android_share_claim_page_universe,ig_direct_holdout_h2_2018,ig_android_reactive_feed_like_count,ig_android_redirect_to_web_on_oembed_fail_universe,ig_camera_android_facetracker_v12_universe,ig_android_biz_qp_suggest_page,ig_android_direct_mutation_manager_job_scheduler,ig_android_continuous_video_capture,ig_android_live_skin_smooth,ig_promote_net_promoter_score_universe,ig_android_qp_features,ig_android_reel_raven_video_segmented_upload_universe,ig_android_biz_new_choose_category,ig_android_rate_limit_mediafeedviewablehelper,ig_android_shopping_post_tagging_redesign,ig_android_invite_xout_universe,ig_android_direct_permanent_video_upload_length,ig_android_sso_use_trustedapp_universe,ig_mi_impression_mainfeed_switchover,ig_android_remove_follow_all_fb_list,ig_android_save_all,ig_android_vc_call_screen_universe,ig_android_vc_join_timeout_universe,felix_android_video_quality,ig_eof_demarcator_style_universe,ig_shopping_post_insights,ig_android_shopping_more_from_business,ig_android_igtv_feed_trailer,ig_android_skip_video_render,ig_android_highlight_stickers_universe,ig_android_gap_rule_enforcer_universe,ig_android_interactive_listview_during_refresh,ig_android_ffmpeg_muxer_write_retry_universe,ig_android_main_feed_carousels_universe,ig_android_post_recs_show_more_button_universe,ig_android_live_suggested_live_expansion,ig_android_direct_inbox_cache_inbox_row_qes_universe,ig_android_video_cover_frame_universe,ig_android_abr_settings,ig_android_direct_app_hide_recents_header_in_recipient_picker_universe,ig_android_disk_usage_logging_universe,ig_android_story_sharing_universe,ig_android_optic_camera_warmup,ig_android_video_refactor_logger,ig_promote_lotus_universe,ig_stories_engagement_team_holdout_universe,ig_android_stories_gallery_video_segmentation,ig_promote_review_screen_title_universe,ig_android_direct_replace_inbox_camera_with_stories_camera,ig_explore_2018_post_chaining_account_recs_dedupe_universe,ig_android_igtv_save,ig_android_direct_presence_indicator,ig_android_asset_picker_improvements,ig_android_react_native_universe_kill_switch,ig_android_fs_new_gallery,android_ig_live_blacklisting,ig_android_qp_kill_switch,ig_android_new_contact_invites_entry_points_universe,ig_android_optic_feature_testing,ig_android_ad_leadgen_single_screen_universe,ig_android_stories_highlights_fast_navigation_universe,ig_android_vc_add_users_universe,ig_android_react_native_email_sms_settings_universe,ig_android_sticker_search_explorations,ig_android_business_id_conversion_universe,ig_android_business_promote_refresh_fb_access_token_universe,ig_android_selfupdate_jobscheduler,ig_android_fb_url_universe,ig_camera_android_profile_ar_notification_universe,ig_android_story_viewer_linear_preloading_count,ig_live_holdout_h2_2018,ig_android_vc_missed_call_notification_action_call_back,ig_android_stories_tray_in_viewer,ig_android_betamap_universe,ig_android_feed_video_mute_button_position,instagram_aat,ig_login_activity,ig_video_experimental_encoding_consumption_universe,ig_android_stories_share_extension_video_segmentation,ig_camera_android_black_feed_sticker_fix_universe,ig_android_camera_post_smile_low_end_universe,ig_android_import_page_post_after_biz_conversion,ig_android_direct_inbox_rv_configuration_universe,ig_android_feed_upload_progress,ig_vc_h2_2018_holdout_universe,ig_camera_android_superzoom_icon_position_universe,ig_android_live_dash_latency_manager,instagram_interests_holdout,ig_android_user_detail_endpoint,ig_android_click_to_direct_story_reaction_universe,ig_android_shopping_sidecar_editing,ig_android_interactions_new_comment_like_pos_universe,ig_android_reel_tray_item_impression_logging_viewpoint,ig_android_gif_framerate_throttling,ig_android_shopping_checkout_mvp,ig_android_live_save_to_camera_roll_limit_by_screen_size_universe,ig_end_of_feed_universe,ig_android_live_use_all_preview_sizes,ig_promote_post_insights_entry_universe,ig_hero_player,ig_stories_music_themes,ig_android_video_ffmpeg_muxer_universe,ig_android_live_follow_from_comments_universe,ig_android_profile_phone_autoconfirm_universe,ig_android_inline_notifications_recommended_user,ig_android_live_ama_universe,ig_android_camera_use_gl_for_postcapture_type,ig_android_insights_media_hashtag_insight_universe,ig_account_recs_in_chaining,ig_android_igtv_whitelisted_for_web,ig_fb_cross_posting_sender_side_holdout,ig_android_felix_feed_badging_tooltip_universe,ig_camera_gallery_button_thumbnail_universe,ag_family_bridges_2018_h2_holdout,ig_android_arengine_separate_prepare,ig_android_direct_visual_history,ig_android_employee_options_override,ig_android_share_product_universe,ig_camera_android_ar_platform_universe,ig_android_nametag,ig_android_netego_scroll_perf,ig_fbns_preload_default,ig_android_cover_frame_blacklist,android_cameracore_ard_ig_integration,ig_android_use_iterative_box_blur,ig_android_direct_inbox_recyclerview_pool_size,ig_android_clear_inflight_image_request,ig_android_audio_ingestion_params,ig_android_native_logcat_interceptor,ig_android_stories_separate_overlay_creation,ig_android_enable_liger_preconnect_universe,ig_android_hacked_account_reporting,ig_android_high_res_gif_stickers,ig_android_direct_remove_permanent_reactions_bar,ig_android_vod_abr_universe,ig_payments_paypal,ig_android_hashtag_feed_tabbed,ig_android_vc_participants_grid_universe,ig_android_video_decoder_retry,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_account_identity_2018_h2_lockdown_phone_global_holdout,ig_android_one_tap_sharesheet_fb_extensions,ig_android_country_code_fix_universe,ig_android_optic_fast_preview_restart_listener,ig_android_inline_appeal_show_new_content,ig_android_show_su_in_other_users_follow_list,ig_android_fb_family_navigation_badging_user,ig_android_video_scrubber_thumbnail_universe,ig_lockdown_feed_caption_length_universe,ig_camera_android_optimizations_2018_h2_universe,ig_stories_music_sticker,ig_android_optic_disable_post_capture_preview_restart,ig_android_vc_minimized_viewer_universe,ig_android_share_others_post_reorder,ig_android_low_data_mode_backup_5,ig_school_community_v2_universe,ig_android_post_live_expanded_comments_view_universe,ig_android_story_ad_cta_context_universe,ig_android_save_auto_sharing_to_fb_option_on_server,ig_android_igtv_chaining,ig_android_profile_private_banner,ig_android_stories_video_prefetch_kb,ig_android_direct_stories_in_direct_inbox,android_cameracore_preview_frame_listener2_ig_universe,ig_android_live_stop_broadcast_on_404,ig_android_live_skip_live_encoder_pts_correction,ig_android_show_twitter_name_universe,ig_android_direct_new_message_ranking,ig_android_render_iframe_interval,ig_android_direct_allow_multiline_composition,ig_android_place_search_profile_image,live_with_request_to_join_button_universe,ig_story_camera_reverse_video_experiment,ig_android_file_descriptor_limit,ig_android_stories_tray_fast_scroll_universe,ig_android_story_ad_text_limitation_universe,ig_android_cameracore_ar_text_plugin_universe,ig_android_direct_audience_upgrade_in_thread_camera,ig_android_felix,ig_android_media_share_icon,ig_android_archive_features_holdout_universe,ig_share_to_story_toggle_include_shopping_product,ig_two_fac_totp_enable,ig_android_camera_universe,ig_android_insights_creative_tutorials_universe,ig_android_qp_slot_cooldown_enabled_universe,ig_android_photos_qpl,ig_android_video_call_finish_universe,ig_hashtag_following_holdout_universe,ig_android_facebook_global_state_sync_frequency_universe,ig_android_global_scheduler_direct,ig_android_unify_video_player,ig_android_webrtc_icerestart_universe,ig_android_scroll_stories_tray_to_front_when_stories_ready,ig_android_mi_holdout_h1_2019,ig_android_interactions_permalink_replace_single_media_universe,ig_android_ttcp_improvements,ig_android_live_comment_fetch_frequency_universe,ig_android_directapp_instagram_deeplinking,ig_android_direct_inbox_recyclerview,ig_shopping_viewer_share_action,ig_android_hashtag_row_preparer,ig_eof_caboose_universe,ig_android_optic_new_features_implementation,ig_android_optic_new_zoom_controller,ig_android_direct_log_badge_count_inconsistent,ig_android_qp_clash_management_enabled_v4_universe,ig_android_hide_button_for_invite_facebook_friends,ig_android_activity_feed_impression_logger,ig_android_visualcomposer_inapp_notification_universe,ig_android_direct_sticker_gifs_in_thread,ig_android_optic_surface_texture_cleanup,ig_android_live_align_by_2_universe,ig_android_mobile_boost_universe,ig_android_network_util_cache_info,ig_android_camera_new_early_show_smile_icon_universe,ig_android_ads_profile_cta_feed_universe,ig_android_viewpoint_netego_universe,ig_android_direct_remix_visual_messages,ig_android_camera_new_tray_behavior_universe,ig_android_auto_advance_su_unit_when_scrolled_off_screen,ig_android_business_ix_universe,ig_vp9_hd_blacklist,ig_android_new_one_tap_nux_universe,ig_feed_experience,ig_android_business_new_navigation_universe,ig_stories_injection_tool_enabled_universe,ig_android_direct_import_google_photos2,ig_android_stories_text_format_emphasis,ig_android_direct_app_invites,ig_android_promote_fbauth_universe,ig_android_video_resize_operation,ig_android_stories_loading_automatic_retry,ig_android_live_end_redirect_universe,ig_android_following_hashtags_tooltip,ig_direct_max_participants,ig_android_stories_whatsapp_share,ig_android_low_data_mode_backup_2,ig_android_bitmap_attribution_check,ig_android_contact_invites_nux_universe,ig_android_search_page_v2,ig_android_direct_share_story_to_facebook,ig_android_stories_music_overlay,ig_android_direct_null_state_activation_cards,ig_android_fbupload_sidecar_video_universe,ig_android_tagging_combined_indicator,ig_android_direct_app_thread_presence_header,ig_android_react_native_restart_after_error_universe,ig_android_camera_attribution_in_direct,ig_android_contact_point_upload_rate_limit_killswitch,ig_android_profile,ig_android_additional_contact_in_nux,ig_android_profile_activation_cards_expanded,ig_android_view_and_likes_cta_universe,ig_android_story_reactions_producer_holdout,ig_android_live_use_rtc_upload_universe,ig_android_live_replay_highlights_universe,ig_main_activity_cold_start,ig_android_direct_double_tap_like_everything,ig_android_direct_character_limit,ig_business_dynamic_conversion_universe,ig_android_shopping_channel_in_explore,ig_stories_holdout_h1_2018,ig_android_scroll_perf_qpl_killswitch,ig_android_fbns_optimization_universe,ig_camera_ar_effect_attribution_position,ig_android_video_ta_universe,ig_android_live_view_profile_from_comments_universe,ig_android_interactions_threaded_comments_in_feed_universe,ig_fbns_blocked,ig_android_sso_kototoro_app_universe,ig_android_stories_question_sticker_music_format,ig_android_biz_auto_slide_props,ig_media_account_rollout_universe,ig_android_show_fbunlink_button_based_on_server_data,ig_android_fs_creation_flow_tweaks,ig_android_recommend_accounts_killswitch,ig_android_shopping_save_product_collection_cell_redesign_universe,ig_android_direct_inbox_background_view_models,ig_android_page_claim_deeplink_qe,ig_android_profile_edit_phone_universe,ig_android_switch_back_option,ig_android_new_orders_entrypoint,ig_android_media_rows_async_inflate,ig_android_direct_story_chaining_v2,ig_android_ad_show_full_name_universe,ig_android_private_highlights_universe,ig_android_igtv_audio_always_on,ig_android_interactions_inline_composer_extensions_universe,ig_android_scroll_main_feed,ig_business_integrity_ipc_universe,ig_android_location_page_info_page_upsell,ig_camera_android_bg_processor,ig_android_stories_viewer_prefetch_improvements,ig_android_rate_limit_feed_item_viewable_helper,ig_android_fci_empty_feed_friend_search,ig_feed_requests_logs_universe,ig_android_video_qp_logger_universe,ig_nametag_data_collection,ig_discovery_holdout_universe,ig_android_recyclerview_binder_group_enabled_universe,ig_android_direct_create_shortcut,ig_android_ar_effects_button_display_timing,ig_vc_holdout_universe_h2,ig_android_stories_sampled_progress,ig_android_qpl_queue_time_universe,ig_android_downloadable_vp8_module,ig_android_ccu_jobscheduler_outer,ig_android_stories_viewer_modal_activity,ig_android_direct_thread_composer,ig_android_fbns_preload_direct_universe,ig_android_direct_24h_replayability_nux_killswitch_universe,ig_android_activity_feed_row_click,ig_android_time_spent_dashboard,ig_android_loom_v2,ig_android_ad_pbia_header_click_universe,ig_android_direct_quick_replies,ig_android_handle_username_in_media_urls_universe,ig_android_request_compression_universe,ig_android_live_pip_minimize_universe,ig_android_usersession_leak_patching_universe,ig_android_stories_viewer_tall_android_cap_media_universe,ig_android_growth_fci_team_holdout_universe,ig_android_insights_holdout,ig_feed_engagement_holdout_2018_h1,ig_fb_graph_differentiation_only_fb_candidates,ig_pacing_overriding_universe,ig_android_direct_app_multi_account_badging,ig_android_direct_persisted_text_drafts_universe,ig_android_felix_prefetch_thumbnail_sprite_sheet,ig_camera_android_segmentation_async_universe,ig_android_category_search_in_sign_up,ig_android_separate_network_executor,ig_android_interactions_comment_like_for_all_feed_universe,ig_android_remove_push_notifications,ig_android_video_segment_ffmpeg_muxer_universe,ig_android_downgrade_viewport_exit_behavior,ig_android_vc_call_ended_cleanup_universe,ig_android_universe_video_production,ig_android_intialization_chunk_410,ig_android_live_analytics,ig_android_stories_music_filters,ig_android_camera_gallery_upload_we_universe,ig_android_video_exoplayer_2,ig_android_stories_music_precapture,ig_android_bitmap_compress_retry_universe,ig_android_verified_comments_universe,ig_android_dash_script,ig_android_igtv_feed_banner_redesign,ig_shopping_viewer_intent_actions,ig_android_gallery_order_by_date_taken,ig_android_location_plugin_leak_detection,ig_android_custom_story_import_intent,ig_lockdown_feed_perf,ig_android_camera_ar_platform_profile_universe,ig_stories_allow_camera_actions_while_recording,ig_android_optic_new_architecture,ig_android_ig_to_fb_sync_universe,ig_android_fbc_upsell_on_dp_first_load,ig_android_video_watermark_universe_qe2,ig_android_shopping_video_product_tag_consumption,ig_android_share_others_post_share_sheet,ig_biz_growth_entry_value,ig_android_stories_alignment_guides_universe,ig_android_livewith_guest_adaptive_camera_universe,ig_android_business_transaction_in_stories_creator,ig_android_optic_thread_priorities,ig_android_delayed_comments,ig_profile_company_holdout_h2_2018,ig_android_feed_coldstart_universe,ig_android_felix_pager_center_buffer_bias,ig_android_edit_metadata,ig_android_user_url_deeplink_fbpage_endpoint,ig_android_direct_face_filter_button_in_composer,ig_android_stories_helium_balloon_badging_universe,ig_android_rate_limit_feed_video_module,ig_android_ad_watchbrowse_universe,ig_android_stories_private_mention_sharing_universe,ig_direct_raven_search_universe,ig_android_live_pivot_to_reshare_universe,ig_company_profile_holdout,ig_android_invite_list_button_redesign_universe,ig_android_log_mediacodec_info,ig_android_fb_follow_server_linkage_universe,ig_android_direct_expiring_media_loading_errors,ig_android_direct_remove_blurred_profile_photo_for_thread_camera_universe,ig_camera_regiontracking_use_similarity_tracker_for_scaling,ig_android_not_modified_cache_universe,ig_android_direct_thread_green_dot_presence_universe,ig_igds_snackbar_android_universe,ig_android_insights_relay_optimization_universe,ig_android_stories_viewer_bitmap_holder,ig_android_shopping_catalogsearch,ig_android_location_page_intent_survey,ig_android_reel_zoom_universe,ig_android_biz_suggested_category,ig_android_cpu_frame_rendering_universe,ig_android_stories_create_flow_favorites_tooltip,ig_android_q3lc_transparency_control_settings,ig_android_stories_music_broadcast_receiver,ig_android_direct_send_new_combined_reshare,ig_android_resuming_failed_image_downloads_universe,ig_android_push_notifications_settings_redesign_universe,ig_android_enable_request_compression_ccu,ig_android_vc_ongoing_call_notification_universe,ig_android_stories_helium_long_press_universe,ig_fb_notification_universe,ig_branded_content_paid_branded_content,ig_android_downloadable_igrtc_module,ig_android_hide_reset_with_fb_universe,ig_android_direct_newer_single_line_composer_universe,ig_android_story_decor_image_fbupload_universe,ig_android_hashtag_creation_development,ig_android_ad_view_ads_native_universe,ig_android_hero_player_settings,ig_promote_ppe_v2_universe,ig_android_stories_archive_calendar,ig_android_ad_watchbrowse_cta_universe,ig_android_player_crash_report,ig_business_signup_biz_id_universe,ig_android_video_render_device_tiers,ig_android_payload_based_scheduling,ig_android_realtime_iris,ig_android_direct_gifs_in_thread,ig_android_main_feed_fragment_scroll_timing_histogram_uni,ig_android_direct_inbox_recyclerview_fixedsize_universe,ig_android_qp_batch_fetch_caching_enabled_v1_universe,ig_android_inline_editing_local_prefill,ig_android_location_feed_related_business,ig_promote_audience_selection_universe,ig_android_direct_low_contrast_inbox,ig_android_media_rows_prepare_10_31,ig_android_stories_fix_current_active_item_bound_crash,ig_family_bridges_holdout_universe,ig_android_push_notification_settings_universe,ig_android_updatelistview_on_loadmore,ig_promote_no_create_ads_check_universe,ig_android_business_ix_self_serve,ig_direct_raven_sharesheet_ranking,ig_android_insta_video_consumption_infra,ig_android_api_urlencode_universe,ig_android_concurrent_cold_start_universe,ig_android_direct_inbox_custom_rv_prefetch,ig_android_vc_missed_call_notification_action_reply,ig_android_multi_capture_camera,ig_android_stories_cross_sharing_to_fb_holdout_universe,ig_smb_ads_holdout_2018_h2_universe,instagram_android_stories_sticker_tray_redesign,ig_android_edit_location_page_info,ig_android_felix_video_upload_length,ig_android_video_segment_resume_policy_universe,ig_android_igsystrace_universe,ig_android_direct_split_reshares,ig_android_igtv_banner_changes,ig_android_dash_for_vod_universe,ig_android_new_highlight_button_text,ig_android_video_call_participant_state_caller_universe,ig_android_story_ads_default_long_video_duration,ig_android_stories_camera_enhancements,ig_android_feed_stale_check_interval,ig_find_loaded_classes,ig_android_interactions_realtime_typing_indicator_and_live_comments,ig_android_video_live_trace_universe,ig_android_stories_gallery_improvements,ig_close_friends_v4_global,ig_android_stories_large_reel_navigation,ig_android_prefetch_notification_data,ig_android_3pspp,ig_android_direct_new_intro_card,ig_android_direct_pending_media,ig_camera_ar_image_transform_library,ig_android_live_share_post_live_universe,ig_android_comments_composer_newline_universe,ig_android_direct_mutation_manager_iris,ig_android_stories_gif_sticker,ig_android_interactions_feed_dwell_universe,ig_camera_android_superzoomv3_attribution_universe,ig_android_stories_posting_offline_ui,ig_camera_android_superzoomv3_universe,ig_android_account_hierarchy_account_association_signal_upload_kill_switch,ig_android_offline_mode_holdout,ig_android_comments_direct_reply_to_author,ig_android_video_streaming_upload_universe,ig_direct_holdout_h1_2019,ig_android_stepper_header,ig_android_family_bridge_discover,ig_direct_report_conversation_universe,igds_android_listrow_migration_universe,ig_android_camera_sdk_check_gl_surface_r2,ig_promote_story_insights_entry_universe,ig_android_http_service_same_thread,ig_challenge_general_v2,ig_android_expired_build_lockout,ig_android_felix_keep_video_view,ig_feed_video_autoplay_tap_threshold,ig_android_vpvd_impressions_universe,ig_android_stories_reel_interactive_tap_target_size,ig_android_rendering_controls,ig_android_os_version_blocking,ig_promote_fix_expired_fb_accesstoken_android_universe,ig_android_stories_combined_asset_search,ig_android_interactions_emoji_extension_followup_universe,ig_android_shopping_native_catalog_selection,ig_android_profile_unified_follow_view,ig_android_igtv_no_badge,ig_android_unfollow_from_main_feed_v2,ig_android_livewith_liveswap_optimization_universe,ig_promote_video_retry_universe,ig_android_vc_participant_state_callee_universe,ig_helium_v1,ig_android_buffered_analytics_logger_thread_safe,ig_android_fb_connect_follow_invite_flow,ig_android_video_stitch_after_segmenting_universe,ig_android_enable_swipe_to_dismiss_for_all_dialogs,ig_android_business_cross_post_with_biz_id_infra,ig_android_paid_branded_content_rendering,ig_android_rage_shake_whitelist,ig_android_low_data_mode_backup_4,ig_mi_analytics_uploader_diagnostics,ig_android_shopping_pdp_craft,ig_android_ad_connection_manager_universe,ig_android_skip_button_content_on_connect_fb_universe,ig_android_reset_to_feed_from_background,ig_android_ad_watchbrowse_carousel_universe,android_cameracore_ig_gl_oom_fixes_universe,ig_android_video_feed_universe,ig_android_hybrid_bitmap_version_2,ig_android_update_items_checks,ig_android_interactions_mention_search_presence_dot_universe,ig_android_direct_app_reel_grid_search,ig_android_live_disable_speed_test_ui_timeout_universe,ig_android_hashtag_page_reduced_related_items,ig_android_direct_mutation_manager_media_2,ig_direct_reshare_sharesheet_ranking,ig_android_image_fail_callback_fix_universe,ig_android_igtv_reshare,ig_direct_reshare_search_universe,ig_android_shopping_pdp_platformization,ig_branded_content_share_to_facebook,ig_android_building_aymf_universe,ig_android_stories_viewer_as_modal_high_end_launch,ig_android_collect_os_usage_events_universe,ig_android_shopping_product_appeals_universe,ig_android_direct_mqtt_send,ig_android_business_profile_share_link_universe,ig_android_reliability_leak_fixes_h2_2018,ig_promote_unified_insights_universe,ig_android_global_prefetch_scheduler,ig_fbns_shared,ig_android_stories_reel_media_item_automatic_retry,ig_android_interactions_composer_extensions_universe,ig_android_cache_timespan_objects,ig_android_rn_ads_manager_universe,ig_smb_ads_click_to_direct,ig_android_foreground_location_collection,ig_kill_connectivity_change_receiver,ig_android_pending_actions_serialization,ig_android_2018_h1_hashtag_report_universe,ig_android_new_camera_design_universe,ig_android_prefetch_carousels_on_swipe_universe,ig_android_ads_history_universe,ig_fb_graph_differentiation_top_k_fb_coefficients,ig_explore_2018_topic_channel_navigation_android_universe,ig_android_shopping_profile_tab_universe,ig_android_hashtag_unfollow_from_main_feed,ig_android_ad_watchmore_entry_point_universe,ig_android_stories_feedback_badging_universe,ig_android_low_latency_consumption_universe,ig_android_graphql_survey_new_proxy_universe,ig_android_resumable_downloads_logging_universe,ig_direct_recipients_search_universe,ig_android_scheduled_executor,ig_android_fblocation_universe,ig_promote_rename_to_boost_universe,ig_android_early_storyrequest,ig_android_ad_holdout_watchandmore_universe,ig_android_felix_insights,ig_android_interests_netego_dismiss,ig_android_realtime_always_start_connection_on_condition_universe,ig_android_split_contacts_list,ig_android_igtv_always_show_browse_ui,ig_android_always_use_server_recents,ig_android_carousel_prefetch_bumping,ig_fbns_kill_switch,ig_android_direct_send_thread_summary_fix_universe,ig_android_video_fix_logger,ig_stories_question_sticker_music_format_prompt,ig_mi_extra_bundle_investigation_universe,ig_camera_android_segmentation_qe2_universe,ig_android_direct_media_forwarding,ig_android_stories_close_friends_disable_first_time_badge,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_fb_link_ui_polish_universe,ig_android_signup_error_test,ig_android_video_webrtc_textureview,ig_android_business_promote_tooltip,mi_viewpoint_viewability_universe,ig_android_volume_controls,ig_xplat_shopping_cataloglist,ig_android_interactions_in_feed_comment_view_universe,ig_android_biz_category_prefill_universe,ig_android_pigeon_sampling,ig_android_gallery_high_quality_photo_thumbnails,ig_android_show_weekly_ci_upsell_limit,ig_android_tagging_video_preview,ig_direct_android_reply_modal_universe,ig_ei_option_setting_universe,ig_perf_android_holdout,ig_direct_core_holdout_q1_2018,ig_promote_insights_video_views_universe,ig_android_list_redesign,ig_android_claim_location_page,ig_android_search_normalization,ig_android_not_decoding_prefetch,ig_smb_review_screen_content_update_universe,ig_android_category_search_edit_profile,ig_android_direct_forward_messages_universe,ig_android_pbia_proxy_profile_universe,ig_android_cover_frame_rendering,ig_android_feed_post_sticker_alt,ig_camera_android_segmentation_enabled_universe,ig_android_shopping_profile_shop_redesign,ig_android_upload_retry_job_service,ig_android_stories_better_error_state_handling,ig_android_vc_in_app_notification_universe,ig_android_persistent_duplicate_notif_checker_user_based,ig_android_react_native_ota,ig_android_profile_memories_universe,ig_fb_graph_differentiation_control,ig_android_low_data_mode_backup_3,android_ig_camera_ar_asset_manager_improvements_universe,ig_android_explore_discover_people_entry_point_universe,ig_android_qcc_perf,ig_android_video_cache_evictor_universe,ig_android_limit_ashmem_cleanup_thread,ig_android_direct_business_holdout,ig_android_promote_feed_to_stories_universe,ig_media_geo_gating,ig_music_dash,ig_android_media_as_sticker,ig_android_internal_sticker_universe,ig_android_video_watermark_universe,ig_android_live_ama_viewer_universe,ig_android_live_streaming_experimental_abr_universe,ig_android_cronet_stack,ig_android_mention_sharing_from_reel_viewer_universe,ig_android_warm_headline_text,ig_android_new_block_flow,ig_android_story_landscape_ad_new_layout_universe,ig_android_long_form_video,ig_android_network_trace_migration,ig_android_story_ads_direct_cta_universe,ig_android_live_subscribe_user_level_universe,ig_android_ad_iab_qpl_kill_switch_universe,ig_android_fb_sync_options_universe,ig_android_saved_product_store,ig_android_stories_reappearing_tray_universe,ig_android_new_camera_design_container_animations_universe,ig_android_stories_disable_highlights_media_preloading,ig_fb_graph_differentiation,ig_android_logging_metric_universe_v2,ig_android_stories_persistent_tray_universe,ig_android_screen_recording_bugreport_universe,ig_android_friends_sticker,ig_android_whats_app_contact_invite_universe,ig_android_feed_auto_share_to_facebook_dialog,ig_android_felix_creation_enabled,ig_direct_android_larger_media_reshare_style,ig_android_stories_auto_retry_reels_media_and_segments,ig_android_image_mem_cache_strong_ref_universe,ig_direct_android_inbox_filter_for_all_universe,ig_android_suggested_highlights,ig_direct_giphy_gifs_rating,ig_stories_holdout_h2_2017,ig_android_fbpage_on_profile_side_tray,ig_android_video_server_coverframe,ig_android_video_controls_universe,ig_camera_holdout_h1_2018_performance,ig_android_stories_music_search_typeahead,ig_android_inappnotification_rootactivity_tweak,ig_android_local_info_page,ig_camera_holdout_h1_2018_product,ig_shopping_checkout_mvp_experiment,ig_android_hide_type_mode_camera_button,ig_timestamp_public_test,ig_android_webrtc_renderer_reuse_universe,ig_android_business_conversion_value_prop_v2,ig_android_live_wave_production_universe,ig_android_share_publish_page_universe,ig_android_question_sticker_replied_state,ig_android_early_feedrequest,ig_android_hashtag_search_suggestions,ig_android_hashtag_discover_tab,ig_android_leak_detector_upload_universe,ig_android_hashtag_page_support_places_tab,ig_android_cover_frame_retrieval,ig_android_live_bg_download_face_filter_assets_universe,ig_android_direct_continuous_capture,ig_android_search_hashtag_badges,ig_android_direct_tabbed_media_picker,ig_android_video_ssim_report_universe,ig_android_direct_view_more_qe,ig_camera_android_effect_info_bottom_sheet_universe,ig_promote_add_payment_navigation_universe,ig_android_direct_voice_messaging,ig_android_signup_refactor_santity,ig_android_profile_lazy_load_carousel_media,ig_android_reel_dashboard_camera_entry_point,ig_android_su_follow_back,ig_android_direct_reel_options_entry_point_2_universe,ig_android_ad_redesign_iab_universe,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_modal_activity_no_animation_fix_universe,ig_android_bitmap_cache_executor_size,ig_android_direct_log_badge_count,ig_android_direct_remove_visual_messages_nuxs,ig_android_creation_new_post_title,ig_camera_fast_tti_universe,ig_android_non_square_first,ig_promote_media_picker_universe,ig_android_direct_thread_content_picker,ig_android_vc_fix_joining_other_call_with_new_intent,ig_android_drawable_usage_logging_universe,ig_android_reel_viewer_data_buffer_size,ig_android_hashtag_contextual_feed_account_recs,ig_traffic_routing_universe,ig_promote_political_ads_universe,ig_android_clarify_invite_options,ig_android_igtv_aspect_ratio_limits,ig_android_effect_tray_background,ig_android_disable_scroll_listeners,ig_android_profile_neue_universe,ig_android_create_page_on_top_universe,ig_stories_selfie_sticker,ig_android_video_upload_quality_qe1,ig_android_mobile_http_flow_sampling_weight_universe,ig_android_stories_music_awareness_universe,ig_android_live_nerd_stats_universe,ig_android_video_cache_size_universe,ig_camera_android_focus_attribution_universe,ig_android_promote_story_to_story_universe,ig_android_igds_edit_profile_fields,ig_android_reel_impresssion_cache_key_qe_universe,ig_video_holdout_h2_2017,ig_android_immersive_viewer_follow,ig_android_sso_family_key_universe,ig_android_direct_share_sheet_custom_fast_scroller,ig_android_external_gallery_import_affordance,ufi_share,ig_android_sonar_prober_universe,ig_android_swipe_up_area_universe,ig_android_video_segmented_upload_universe,ig_perf_android_holdout_2018_h1,ig_android_live_special_codec_size_list,ig_android_view_info_universe,ig_android_shopping_combined_tagging_universe,ig_android_cold_start_cool_off_universe,ig_android_shopping_video_product_tag_creation,ig_android_startup_sampling_rate_universe,ig_android_igtv_new_browse,ig_android_story_import_intent,ig_android_direct_inbox_typing_indicator,ig_android_edit_highlight_redesign,ig_android_insta_video_broadcaster_infra_perf,ig_android_live_webrtc_livewith_params,ig_android_show_fb_name_universe,ig_android_fix_prepare_direct_push,ig_android_stories_viewer_responsiveness_universe,ig_android_interactions_show_verified_badge_for_preview_comments_universe,ig_android_stories_skip_preload_to_launch_viewer,ig_android_live_start_live_button_universe,ig_android_direct_speed_cam_univ,ig_android_profile_menu_reorder_universe,ig_android_acra_double_oom_reservation,ig_android_live_viewer_tap_to_hide_chrome_universe,ig_android_vc_sounds_universe,ig_android_igtv_native_pip,ig_android_igtv_refresh_tv_guide_interval,ig_direct_inbox_search_universe,ig_android_experimental_onetap_dialogs_universe,ig_android_pendingmedia_retry,ig_android_settings_redesign,ig_android_direct_search_story_recipients_universe,ig_android_fb_sharing_shortcut,ig_android_direct_segmented_video,ig_android_grid_cell_count,ig_android_ad_watchinstall_universe,ig_android_realtime_manager_optimization,ig_android_shortcuts,ig_android_comments_notifications_universe,ig_android_vc_webrtc_params,ig_android_critical_path_manager_universe,ig_android_canvas_tilt_to_pan_universe,ig_android_feed_sharing_memory_leak,ig_android_ad_account_top_followers_universe,ig_android_offline_reel_feed,ig_promote_review_screen_universe,ig_android_vc_end_screen_user_feedback_universe,ig_android_vc_use_timestamp_normalizer,native_contact_invites_universe,ig_android_feed_post_sticker,ig_android_facebook_crosspost,ig_android_local_2018_h2_holdout,ig_android_stories_tray_refresh_universe,ig_android_viewer_tapback_size_universe,ig_android_nametag_save_experiment_universe,ig_promote_estimated_clicks_universe,ig_business_profile_18h1_holdout_universe,ig_android_nearby_venues_location_timeout_fallback,ig_android_category_clickable_rows_ui,ig_android_photo_invites,ig_interactions_h2_2018_team_holdout_universe,ig_branded_content_tagging_upsell,ig_android_ccu_jobscheduler_inner,ig_android_story_ads_instant_sub_impression_universe,ig_explore_2018_finite_chain_android_universe,ig_android_gqls_typing_indicator,ig_android_direct_visual_message_prefetch_count_universe,ig_android_webrtc_encoder_factory_universe,ig_ads_increase_connection_step2_v2,ig_scroll_by_two_cards_for_suggested_invite_universe,ig_android_internal_collab_save'  # noqa


class Login(object):
    API_URL = 'https://i.instagram.com/api/{version!s}/'
    USER_AGENT = Constants.USER_AGENT
    IG_SIG_KEY = Constants.IG_SIG_KEY
    IG_CAPABILITIES = Constants.IG_CAPABILITIES
    SIG_KEY_VERSION = Constants.SIG_KEY_VERSION
    APPLICATION_ID = Constants.APPLICATION_ID

    def __init__(self, username, password, **kwargs):
        """

        :param username: Login username
        :param password: Login password
        :param kwargs: See below

        :Keyword Arguments:
            - **auto_patch**: Patch the api objects to match the public API. Default: False
            - **drop_incompat_key**: Remove api object keys that is not in the public API. Default: False
            - **timeout**: Timeout interval in seconds. Default: 15
            - **api_url**: Override the default api url base
            - **cookie**: Saved cookie string from a previous session
            - **settings**: A dict of settings from a previous session
            - **on_login**: Callback after successful login
            - **proxy**: Specify a proxy ex: 'http://127.0.0.1:8888' (ALPHA)
            - **proxy_handler**: Specify your own proxy handler
        :return:
        """
        self.username = username
        self.password = password
        self.auto_patch = kwargs.pop('auto_patch', False)
        self.drop_incompat_keys = kwargs.pop('drop_incompat_keys', False)
        self.api_url = kwargs.pop('api_url', None) or self.API_URL
        self.timeout = kwargs.pop('timeout', 15)
        self.on_login = kwargs.pop('on_login', None)
        self.logger = logger

        user_settings = kwargs.pop('settings', None) or {}
        self.uuid = (
                kwargs.pop('guid', None) or kwargs.pop('uuid', None) or
                user_settings.get('uuid') or self.generate_uuid(False))
        self.device_id = (
                kwargs.pop('device_id', None) or user_settings.get('device_id') or
                self.generate_deviceid())
        # application session ID
        self.session_id = (
                kwargs.pop('session_id', None) or user_settings.get('session_id') or
                self.generate_uuid(False))
        self.signature_key = (
                kwargs.pop('signature_key', None) or user_settings.get('signature_key') or
                self.IG_SIG_KEY)
        self.key_version = (
                kwargs.pop('key_version', None) or user_settings.get('key_version') or
                self.SIG_KEY_VERSION)
        self.ig_capabilities = (
                kwargs.pop('ig_capabilities', None) or user_settings.get('ig_capabilities') or
                self.IG_CAPABILITIES)
        self.application_id = (
                kwargs.pop('application_id', None) or user_settings.get('application_id') or
                self.APPLICATION_ID)

        # to maintain backward compat for user_agent kwarg
        custom_ua = kwargs.pop('user_agent', '') or user_settings.get('user_agent')
        if custom_ua:
            self.user_agent = custom_ua
        else:
            self.app_version = (
                    kwargs.pop('app_version', None) or user_settings.get('app_version') or
                    Constants.APP_VERSION)
            self.android_release = (
                    kwargs.pop('android_release', None) or user_settings.get('android_release') or
                    Constants.ANDROID_RELEASE)
            self.android_version = int(
                kwargs.pop('android_version', None) or user_settings.get('android_version') or
                Constants.ANDROID_VERSION)
            self.phone_manufacturer = (
                    kwargs.pop('phone_manufacturer', None) or user_settings.get('phone_manufacturer') or
                    Constants.PHONE_MANUFACTURER)
            self.phone_device = (
                    kwargs.pop('phone_device', None) or user_settings.get('phone_device') or
                    Constants.PHONE_DEVICE)
            self.phone_model = (
                    kwargs.pop('phone_model', None) or user_settings.get('phone_model') or
                    Constants.PHONE_MODEL)
            self.phone_dpi = (
                    kwargs.pop('phone_dpi', None) or user_settings.get('phone_dpi') or
                    Constants.PHONE_DPI)
            self.phone_resolution = (
                    kwargs.pop('phone_resolution', None) or user_settings.get('phone_resolution') or
                    Constants.PHONE_RESOLUTION)
            self.phone_chipset = (
                    kwargs.pop('phone_chipset', None) or user_settings.get('phone_chipset') or
                    Constants.PHONE_CHIPSET)
            self.version_code = (
                    kwargs.pop('version_code', None) or user_settings.get('version_code') or
                    Constants.VERSION_CODE)

        cookie_string = kwargs.pop('cookie', None) or user_settings.get('cookie')
        cookie_jar = ClientCookieJar(cookie_string=cookie_string)

        cookie_handler = compat_urllib_request.HTTPCookieProcessor(cookie_jar)
        #
        proxy_handler = kwargs.pop('proxy_handler', None)
        if not proxy_handler:
            proxy = kwargs.pop('proxy', None)
            if proxy:
                warnings.warn('Proxy support is alpha.', UserWarning)
                parsed_url = compat_urllib_parse_urlparse(proxy)
                if parsed_url.netloc and parsed_url.scheme:
                    proxy_address = '{0!s}://{1!s}'.format(parsed_url.scheme, parsed_url.netloc)
                    proxy_handler = compat_urllib_request.ProxyHandler({'https': proxy_address})
                else:
                    raise ValueError('Invalid proxy argument: {0!s}'.format(proxy))
        handlers = []
        if proxy_handler:
            handlers.append(proxy_handler)

        # Allow user to override custom ssl context where possible
        custom_ssl_context = kwargs.pop('custom_ssl_context', None)
        try:
            https_handler = compat_urllib_request.HTTPSHandler(context=custom_ssl_context)
        except TypeError:
            # py version < 2.7.9
            https_handler = compat_urllib_request.HTTPSHandler()

        handlers.extend([
            compat_urllib_request.HTTPHandler(),
            https_handler,
            cookie_handler])
        opener = compat_urllib_request.build_opener(*handlers)
        opener.cookie_jar = cookie_jar
        self.opener = opener

        # opener = requests.session()
        # opener.cookie_jar = cookie_jar
        # self.opener = opener

        # ad_id must be initialised after cookie_jar/opener because
        # it relies on self.authenticated_user_name
        self.ad_id = (
                kwargs.pop('ad_id', None) or user_settings.get('ad_id') or
                self.generate_adid())

        # if not cookie_string:
        #     if not self.username or not self.password:
        #         print('login_required')
        #     self.login()
        # #
        # self.logger.debug('USERAGENT: {0!s}'.format(self.user_agent))
        # super(Login, self).__init__()

    def login(self):
        """Login."""

        prelogin_params = self._call_api(
            'si/fetch_headers/',
            params='',
            query={'challenge_type': 'signup', 'guid': self.generate_uuid(True)},
            return_response=True)

        if not self.csrftoken:
            print('Unable to get csrf from prelogin.')
        login_params = {
            'device_id': self.device_id,
            'guid': self.uuid,
            'adid': self.ad_id,
            'phone_id': self.phone_id,
            '_csrftoken': self.csrftoken,
            'username': self.username,
            'password': self.password,
            'login_attempt_count': '0',
        }

        login_response = self._call_api(
            'accounts/login/', params=login_params, return_response=True)

        if not self.csrftoken:
            print('Unable to get csrf from login.')
        if login_response:
            login_json = json.loads(self._read_response(login_response))
            if not login_json.get('logged_in_user', {}).get('pk'):
                raise print('Unable to login.')

    def user_info(self, user_id):
        """
        Get user info for a specified user id

        :param user_id:
        :return:
        """
        res = self._call_api('users/{user_id!s}/info/'.format(**{'user_id': user_id}))
        return res

    def user_detail_info(self, user_id, **kwargs):
        """
        EXPERIMENTAL ENDPOINT, INADVISABLE TO USE.
        Get user detailed info

        :param user_id:
        :param kwargs:
            - **max_id**: For pagination
            - **min_timestamp**: For pagination
        :return:
        """
        warnings.warn('This endpoint is experimental. Do not use.')

        endpoint = 'users/{user_id!s}/full_detail_info/'.format(**{'user_id': user_id})
        res = self._call_api(endpoint, query=kwargs)

        return res

    def friendships_create(self, user_id):
        """
        Follow a user

        :param user_id: User id
        :return:
            .. code-block:: javascript

                {
                    "status": "ok",
                    "friendship_status": {
                        "incoming_request": false,
                        "followed_by": false,
                        "outgoing_request": false,
                        "following": true,
                        "blocking": false,
                        "is_private": false
                    }
                }
        """
        endpoint = 'friendships/create/{user_id!s}/'.format(**{'user_id': user_id})

        params = {'user_id': user_id, 'radio_type': self.radio_type}
        print(params)
        params.update(self.authenticated_params)
        print(params)
        res = self._call_api(endpoint, params=params)
        return res

    def friendships_destroy(self, user_id, **kwargs):
        """
        Unfollow a user

        :param user_id: User id
        :param kwargs:
        :return:
            .. code-block:: javascript

                {
                    "status": "ok",
                    "incoming_request": false,
                    "is_blocking_reel": false,
                    "followed_by": false,
                    "is_muting_reel": false,
                    "outgoing_request": false,
                    "following": false,
                    "blocking": false,
                    "is_private": false
                }
        """
        endpoint = 'friendships/destroy/{user_id!s}/'.format(**{'user_id': user_id})
        params = {'user_id': user_id, 'radio_type': self.radio_type}
        params.update(self.authenticated_params)
        res = self._call_api(endpoint, params=params)
        return res

    def autocomplete_user_list(self):
        """User list for autocomplete"""
        res = self._call_api(
            'friendships/autocomplete_user_list/',
            query={'followinfo': 'True', 'version': '2'})
        if self.auto_patch:
            [ClientCompatPatch.list_user(user, drop_incompat_keys=self.drop_incompat_keys)
             for user in res['users']]
        return res

    def user_following(self, user_id, rank_token, **kwargs):
        """
        Get user followings

        :param user_id:
        :param rank_token: Required for paging through a single feed and can be generated with
            :meth:`generate_uuid`. You should use the same rank_token for paging through a single user following.
        :param kwargs:
            - **query**: Search within the user following
            - **max_id**: For pagination
        :return:
        """
        raise_if_invalid_rank_token(rank_token)

        endpoint = 'friendships/{user_id!s}/following/'.format(**{'user_id': user_id})
        query_params = {
            'rank_token': rank_token,
        }
        query_params.update(kwargs)
        res = self._call_api(endpoint, query=query_params)
        if self.auto_patch:
            [ClientCompatPatch.list_user(u, drop_incompat_keys=self.drop_incompat_keys)
             for u in res.get('users', [])]
        return res

    def user_followers(self, user, end_cursor=None):
        user_id = Get_Id(f'https://www.instagram.com/{user}/')
        if end_cursor is None:
            strHtml = self.opener.open(
                f"https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={user_id}&first=100")
        else:
            strHtml = self.opener.open(
                f"https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={user_id}&first=100&after={end_cursor}")

        resp = json.loads(strHtml.read())
        return resp

    @property
    def settings(self):
        """Helper property that extracts the settings that you should cache
        in addition to username and password."""
        return {
            'uuid': self.uuid,
            'device_id': self.device_id,
            'ad_id': self.ad_id,
            'session_id': self.session_id,
            'cookie': self.cookie_jar.dump(),
            'created_ts': int(time.time())
        }

    @property
    def user_agent(self):
        """Returns the useragent string that the client is currently using."""
        return Constants.USER_AGENT_FORMAT.format(**{
            'app_version': self.app_version,
            'android_version': self.android_version,
            'android_release': self.android_release,
            'brand': self.phone_manufacturer,
            'device': self.phone_device,
            'model': self.phone_model,
            'dpi': self.phone_dpi,
            'resolution': self.phone_resolution,
            'chipset': self.phone_chipset,
            'version_code': self.version_code})

    @user_agent.setter
    def user_agent(self, value):
        """Override the useragent string with your own"""
        mobj = re.search(Constants.USER_AGENT_EXPRESSION, value)
        if not mobj:
            raise ValueError('User-agent specified does not fit format required: {0!s}'.format(
                Constants.USER_AGENT_EXPRESSION))
        self.app_version = mobj.group('app_version')
        self.android_release = mobj.group('android_release')
        self.android_version = int(mobj.group('android_version'))
        self.phone_manufacturer = mobj.group('manufacturer')
        self.phone_device = mobj.group('device')
        self.phone_model = mobj.group('model')
        self.phone_dpi = mobj.group('dpi')
        self.phone_resolution = mobj.group('resolution')
        self.phone_chipset = mobj.group('chipset')
        self.version_code = mobj.group('version_code')

    @staticmethod
    def generate_useragent(**kwargs):
        """
        Helper method to generate a useragent string based on device parameters

        :param kwargs:
            - **app_version**
            - **android_version**
            - **android_release**
            - **brand**
            - **device**
            - **model**
            - **dpi**
            - **resolution**
            - **chipset**
        :return: A compatible user agent string
        """
        return Constants.USER_AGENT_FORMAT.format(**{
            'app_version': kwargs.pop('app_version', None) or Constants.APP_VERSION,
            'android_version': int(kwargs.pop('android_version', None) or Constants.ANDROID_VERSION),
            'android_release': kwargs.pop('android_release', None) or Constants.ANDROID_RELEASE,
            'brand': kwargs.pop('phone_manufacturer', None) or Constants.PHONE_MANUFACTURER,
            'device': kwargs.pop('phone_device', None) or Constants.PHONE_DEVICE,
            'model': kwargs.pop('phone_model', None) or Constants.PHONE_MODEL,
            'dpi': kwargs.pop('phone_dpi', None) or Constants.PHONE_DPI,
            'resolution': kwargs.pop('phone_resolution', None) or Constants.PHONE_RESOLUTION,
            'chipset': kwargs.pop('phone_chipset', None) or Constants.PHONE_CHIPSET,
            'version_code': kwargs.pop('version_code', None) or Constants.VERSION_CODE})

    @staticmethod
    def validate_useragent(value):
        """
        Helper method to validate a useragent string for format correctness

        :param value:
        :return:
        """
        mobj = re.search(Constants.USER_AGENT_EXPRESSION, value)
        if not mobj:
            raise ValueError(
                'User-agent specified does not fit format required: {0!s}'.format(
                    Constants.USER_AGENT_EXPRESSION))
        parse_params = {
            'app_version': mobj.group('app_version'),
            'android_version': int(mobj.group('android_version')),
            'android_release': mobj.group('android_release'),
            'brand': mobj.group('manufacturer'),
            'device': mobj.group('device'),
            'model': mobj.group('model'),
            'dpi': mobj.group('dpi'),
            'resolution': mobj.group('resolution'),
            'chipset': mobj.group('chipset'),
            'version_code': mobj.group('version_code'),
        }
        return {
            'user_agent': Constants.USER_AGENT_FORMAT.format(**parse_params),
            'parsed_params': parse_params
        }

    def get_cookie_value(self, key, domain=''):
        now = int(time.time())
        eternity = now + 100 * 365 * 24 * 60 * 60  # future date for non-expiring cookies
        if not domain:
            domain = compat_urllib_parse_urlparse(self.API_URL).netloc

        for cookie in sorted(
                self.cookie_jar, key=lambda c: c.expires or eternity, reverse=True):
            # don't return expired cookie
            if cookie.expires and cookie.expires < now:
                continue
            # cookie domain may be i.instagram.com or .instagram.com
            cookie_domain = cookie.domain
            # simple domain matching
            if cookie_domain.startswith('.'):
                cookie_domain = cookie_domain[1:]
            if not domain.endswith(cookie_domain):
                continue

            if cookie.name.lower() == key.lower():
                return cookie.value

        return None

    @property
    def csrftoken(self):
        """The client's current csrf token"""
        return self.get_cookie_value('csrftoken')

    @property
    def token(self):
        """For compatibility. Equivalent to :meth:`csrftoken`"""
        return self.csrftoken

    @property
    def authenticated_user_id(self):
        """The current authenticated user id"""
        return self.get_cookie_value('ds_user_id')

    @property
    def authenticated_user_name(self):
        """The current authenticated user name"""
        return self.get_cookie_value('ds_user')

    @property
    def phone_id(self):
        """Current phone ID. For use in certain functions."""
        return self.generate_uuid(return_hex=False, seed=self.device_id)

    @property
    def timezone_offset(self):
        """Timezone offset in seconds. For use in certain functions."""
        return int(round((datetime.now() - datetime.utcnow()).total_seconds()))

    @property
    def rank_token(self):
        if not self.authenticated_user_id:
            return None
        return '{0!s}_{1!s}'.format(self.authenticated_user_id, self.uuid)

    @property
    def authenticated_params(self):
        return {
            '_csrftoken': self.csrftoken,
            '_uuid': self.uuid,
            '_uid': self.authenticated_user_id
        }

    @property
    def cookie_jar(self):
        """The client's cookiejar instance."""
        return self.opener.cookie_jar

    @property
    def default_headers(self):
        return {
            'User-Agent': self.user_agent,
            'Connection': 'close',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate',
            'X-IG-Capabilities': self.ig_capabilities,
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Connection-Speed': '{0:d}kbps'.format(random.randint(1000, 5000)),
            'X-IG-App-ID': self.application_id,
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-FB-HTTP-Engine': Constants.FB_HTTP_ENGINE,
        }

    @property
    def radio_type(self):
        """For use in certain endpoints"""
        return 'wifi-none'

    def _generate_signature(self, data):
        """
        Generates the signature for a data string

        :param data: content to be signed
        :return:
        """
        return hmac.new(
            self.signature_key.encode('ascii'), data.encode('ascii'),
            digestmod=hashlib.sha256).hexdigest()

    @classmethod
    def generate_uuid(cls, return_hex=False, seed=None):
        """
        Generate uuid

        :param return_hex: Return in hex format
        :param seed: Seed value to generate a consistent uuid
        :return:
        """
        if seed:
            m = hashlib.md5()
            m.update(seed.encode('utf-8'))
            new_uuid = uuid.UUID(m.hexdigest())
        else:
            new_uuid = uuid.uuid1()
        if return_hex:
            return new_uuid.hex
        return str(new_uuid)

    @classmethod
    def generate_deviceid(cls, seed=None):
        """
        Generate an android device ID

        :param seed: Seed value to generate a consistent device ID
        :return:
        """
        return 'android-{0!s}'.format(cls.generate_uuid(True, seed)[:16])

    def generate_adid(self, seed=None):
        """
        Generate an Advertising ID based on the login username since
        the Google Ad ID is a personally identifying but resettable ID.

        :return:
        """
        modified_seed = seed or self.authenticated_user_name or self.username
        if modified_seed:
            # Do some trivial mangling of original seed
            sha2 = hashlib.sha256()
            sha2.update(modified_seed.encode('utf-8'))
            modified_seed = sha2.hexdigest()
        return self.generate_uuid(False, modified_seed)

    @staticmethod
    def _read_response(response):
        """
        Extract the response body from a http response.

        :param response:
        :return:
        """
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            res = gzip.GzipFile(fileobj=buf).read().decode('utf8')
        else:
            res = response.read().decode('utf8')
        return res

    def _call_api(self, endpoint, params=None, query=None, return_response=False, unsigned=False, version='v1'):

        """
        Calls the private api.

        :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
        :param params: POST parameters
        :param query: GET url query parameters
        :param return_response: return the response instead of the parsed json object
        :param unsigned: use post params as-is without signing
        :param version: for the versioned api base url. Default 'v1'.
        :return:
        """
        url = '{0}{1}'.format(self.api_url.format(version=version), endpoint)
        if query:
            url += ('?' if '?' not in endpoint else '&') + compat_urllib_parse.urlencode(query)

        headers = self.default_headers
        data = None
        print(url)
        if params or params == '':
            headers['Content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            if params == '':  # force post if empty string
                data = ''.encode('ascii')
            else:
                if not unsigned:
                    json_params = json.dumps(params, separators=(',', ':'))
                    hash_sig = self._generate_signature(json_params)
                    post_params = {
                        'ig_sig_key_version': self.key_version,
                        'signed_body': hash_sig + '.' + json_params
                    }
                else:
                    # direct form post
                    post_params = params
                data = compat_urllib_parse.urlencode(post_params).encode('ascii')
        print(headers)
        print(data)
        print(url)
        req = compat_urllib_request.Request(url, data, headers=headers)
        try:
            self.logger.debug('REQUEST: {0!s} {1!s}'.format(url, req.get_method()))
            self.logger.debug('DATA: {0!s}'.format(data))
            response = self.opener.open(req, timeout=self.timeout)

            if return_response:
                return response

            response_content = self._read_response(response)
            self.logger.debug('RESPONSE: {0:d} {1!s}'.format(response.code, response_content))
            json_response = json.loads(response_content)

            if json_response.get('message', '') == 'login_required':
                print(
                    json_response.get('message'))

            # not from oembed or an ok response
            if not json_response.get('provider_url') and json_response.get('status', '') != 'ok':
                print(
                    json_response.get('message', 'Unknown error'))

            return json_response

        except compat_urllib_error.HTTPError as e:
            error_response = self._read_response(e)
            self.logger.debug('RESPONSE: {0:d} {1!s}'.format(e.code, error_response))
            print(e, error_response)

        except (SSLError, timeout, SocketError,
                compat_urllib_error.URLError,  # URLError is base of HTTPError
                compat_http_client.HTTPException,
                ConnectionError) as connection_error:
            print('{} {}'.format(
                connection_error.__class__.__name__, str(connection_error)))


app = Login('201028946519', 'ammar2020')
# app = Login('3mora534', 'ammar2200')
# app.login()
app.friendships_create(5535981195)
# end_cursor = None
# u = True
# while u:
#     rq = app.user_followers('chhc', end_cursor=end_cursor)
#     u = rq['data']['user']['edge_followed_by']['page_info']['has_next_page']
#     r = rq['data']['user']['edge_followed_by']['edges']
#     end_cursor = rq['data']['user']['edge_followed_by']['page_info']['end_cursor']
#     for i in r:
#         id = i['node']['id']
#         print(id)
#         r = app.user_info(id)
#         print(r.get('user').get('public_phone_number', {}),
#               r.get('user').get('contact_phone_number', {}),
#               r.get('user').get('public_email', {}))
