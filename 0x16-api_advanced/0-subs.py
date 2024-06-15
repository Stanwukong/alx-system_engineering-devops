#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers
    or a given subreddit.

    Args:
        subreddit (str): Then name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
