import requests
import base64
session = requests.Session()
token = 'Your token or None'
session.headers['Authorization'] = f'token {token}'


def Download(name, url):
    res = session.get(url)
    content = res.json().get('content')
    encoding = res.json().get('encoding')
    with open(name, 'wb') as f:
        f.write(base64.b64decode(content))


def Repos(repos='Downloader', user='3mora2'):
    r = session.get(f'https://api.github.com/repos/{user}/{repos}/contents')
    for cont in r.json():
        if cont.get('type') == 'dir':
            name_dir = cont.get('name')
            dir_url = cont.get('git_url')
            direc = session.get(dir_url)
            for tree in direc.json().get('tree'):
                name_tree = tree.get('path')
                tree_url = tree.get('url')
                print(name_dir, name_tree, tree_url)
        else:
            name = cont.get('name')
            url = cont.get('git_url')
            print(name, url)
            # Download(name, url)

Repos()