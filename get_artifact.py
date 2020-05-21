import requests
import os
import sys

auth = {
    'Authorization': 'token {}'.format(os.environ.get('ACCESS_TOKEN'))
}
url = 'https://api.github.com/repos/{}/actions/artifacts'.format(os.environ.get('GITHUB_REPOSITORY'))
artifact_name = sys.argv[1]

r = requests.get(url, headers=auth)
artifacts = r.json()['artifacts']

for i in artifacts:
    if i['name'] == artifact_name:
        r = requests.get(i['archive_download_url'], headers=auth)
        open('{}.zip'.format(artifact_name), 'wb').write(r.content)
        print('{} downloaded'.format(artifact_name))
        break
else:
    raise Exception('{} is not found'.format(artifact_name))
