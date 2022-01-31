"""Gets list of releases from GitHub"""
import re
from typing import List
import requests


def get_github_releases(url: str) -> List:
    """Takes a URL or organization and repo and returns a list of all releases."""
    output = []

    if "/releases" in url:
        response = requests.get(url).json()
    elif "https://github.com/" in url:
        repo = url.replace("https://github.com/", "")
        response = requests.get(f"https://api.github.com/repos/{repo}/releases").json()
    else:
        pat = re.compile("https://api.github.com/repos/(.*)/releases")
        match = pat.search(url)

        if match is None:
            data = url.split("/")

            if len(data) != 2:
                raise Exception("Could not parse " + url)
        else:
            data = match.group(1).split("/")

        response = requests.get(f"https://api.github.com/repos/{data[0]}/{data[1]}/releases").json()

    for item in response:
        output.append(item["name"])
    return output
