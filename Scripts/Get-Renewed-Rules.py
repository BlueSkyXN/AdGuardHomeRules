import requests
import os

def download_file(url, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as output_file:
        output_file.write(response.content)
    print(f"File downloaded and saved at: {os.path.abspath(filename)}")

files_to_download = {
    "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt": "Renew/cjx-annoyance.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt": "Renew/anti-ad-adguard.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt": "Renew/anti-ad-easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt": "Renew/easyprivacy.txt",
    "https://easylist.to/easylist/easylist.txt": "Renew/easylist.txt",
    "https://easylist-downloads.adblockplus.org/easylistchina.txt": "Renew/easylistchina.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt": "Renew/halflife.txt",
    "https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/hosts.txt": "Renew/scamblocklist-host.txt",
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/AWAvenue-Ads-Rule.txt": "Renew/AWAvenue-Ads-Rule.txt",
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts": "Renew/StevenBlack.txt"
}

for url, filename in files_to_download.items():
    download_file(url, filename)
