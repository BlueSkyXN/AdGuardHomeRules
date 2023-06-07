import requests
import os

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as output_file:
        output_file.write(response.content)

files_to_download = {
    "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt": "cjx-annoyance.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt": "anti-ad-adguard.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt": "anti-ad-easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt": "easyprivacy.txt",
    "https://easylist.to/easylist/easylist.txt": "easylist.txt",
    "https://easylist-downloads.adblockplus.org/easylistchina.txt": "easylistchina.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt": "halflife.txt",
    "https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/hosts.txt": "scamblocklist-host.txt",
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts": "StevenBlack.txt"
}

for url, filename in files_to_download.items():
    download_file(url, os.path.join("..", "Renew", filename))
