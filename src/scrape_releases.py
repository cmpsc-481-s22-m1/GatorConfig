import requests
from typing import List

def get_github_releases(url: str) -> List:
    output = []
    r = ""
    if "https://api.github.com/repos/"  and "/releases" in url:
        r = requests.get(url).json()
    else:
        repo = url.replace("https://github.com/", "")
        r = requests.get(f"https://api.github.com/{repo}/releases")
    for item in r:
        output.append(item["name"])
    return output