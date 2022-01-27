"""Module to test scrape releases"""
import pytest
from gatorconfig.scrape_releases import get_github_releases

@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://api.github.com/repos/GatorEducator/GatorGrader/releases", ["v1.0.0", "v1.0.1"]),
        ("GatorEducator/GatorGrader", ["v1.0.0", "v1.0.1"]),
        ("https://github.com/GatorEducator/gatorgrader", ["v1.0.0", "v1.0.1"]),
    ],
)
def test_get_github_release(requests_mock, url, expected):
    """Tests successful get_github_release requests"""
    requests_mock.get("https://api.github.com/repos/GatorEducator/GatorGrader/releases",
                      json=[{"name": "v1.0.0"}, {"name": "v1.0.1"}])
    assert get_github_releases(url) == expected

@pytest.mark.parametrize(
    "url",
    [
        ("/GatorEducator/GatorGrader/")
    ],
)
def test_get_github_release_fail(requests_mock, url):
    """Tests unsuccessful get_github_release requests"""
    requests_mock.get("https://api.github.com/repos/GatorEducator/GatorGrader/releases",
                      json=[{"name": "v1.0.0"}, {"name": "v1.0.1"}])
    with pytest.raises(Exception):
        get_github_releases(url)
