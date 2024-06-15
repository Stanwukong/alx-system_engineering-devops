#!/usr/bin/python3
"""
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Query the Reddit API and return the top ten hottest posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        posts ([str]): The title of the 10 most popular posts for
        the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10"\
          .format(subreddit)
    headers = {"User-Agent": "Stanwukong"}
    res = requests.get(url, headers=headers)
    try:
        data = res.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
