import os
import sys

import requests

# 每个条目：路径 -> 下载地址（可配置多个备用地址，按顺序尝试）
# 说明：原 halflife 源 https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt
#      因上游账号 o0HalfLife0o 注销（HTTP 404）已失效，改用以下同源镜像。
files_to_download = {
    "Renew/cjx-annoyance.txt": [
        "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt",
    ],
    "Renew/anti-ad-adguard.txt": [
        "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt",
    ],
    "Renew/anti-ad-easylist.txt": [
        "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt",
    ],
    "Renew/easyprivacy.txt": [
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    ],
    "Renew/easylist.txt": [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist-downloads.adblockplus.org/easylist.txt",
    ],
    "Renew/easylistchina.txt": [
        "https://easylist-downloads.adblockplus.org/easylistchina.txt",
    ],
    "Renew/halflife.txt": [
        "https://raw.githubusercontent.com/sbwml/halflife-list/master/ad.txt",
        "https://cdn.jsdelivr.net/gh/sbwml/halflife-list@master/ad.txt",
    ],
    "Renew/scamblocklist-host.txt": [
        "https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/hosts.txt",
    ],
    "Renew/AWAvenue-Ads-Rule.txt": [
        "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/AWAvenue-Ads-Rule.txt",
        "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt",
    ],
    "Renew/StevenBlack.txt": [
        "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    ],
}

TIMEOUT = 60


def download_file(urls, filename):
    """依次尝试 urls 中的地址，成功后写入 filename。

    不再因单个源失败而中断整个流程：全部地址都失败时保留仓库中已有文件
    （由 actions/checkout 提供），并返回 False。
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    for url in urls:
        try:
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            if not response.content:
                raise ValueError("empty response body")
            with open(filename, "wb") as output_file:
                output_file.write(response.content)
            print(f"File downloaded and saved at: {os.path.abspath(filename)}")
            return True
        except Exception as exc:
            print(f"  [WARN] {url} -> {exc}")

    if os.path.exists(filename):
        print(f"  [KEEP] all sources failed, keeping existing file: {filename}")
        return False
    print(f"  [FATAL] all sources failed and no existing file: {filename}")
    return None


def main():
    failed = []
    for filename, urls in files_to_download.items():
        print(f"Downloading {filename} ...")
        result = download_file(urls, filename)
        if result is False:
            failed.append(filename)
        elif result is None:
            return 1

    if failed:
        print()
        print("WARNING: the following files could not be refreshed and were kept as-is:")
        for name in failed:
            print(f"  - {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
