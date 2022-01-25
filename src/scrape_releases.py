import requests
from typing import List

def get_github_releases(url: str) -> List:
    output = []
    r = requests.get("https://api.github.com/repos/gatoreducator/gatorgrader/releases").json()
    for item in r:
        output.append(item["name"])
    return output