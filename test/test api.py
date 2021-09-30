import json, requests

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
    client_id='ZQO5LY3T3TS04AAJJUHLXB03YCLSCSIN4LT0J5YKK31IYLJ5',
    client_secret='PAM2PSRHUOLTFRLH1CBKIDIL35HCE25ICO50Q0WCOR0HF2SO',
    v='20180323',
    ll='40.7243,-74.0018',
    query='coffee',
    limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
