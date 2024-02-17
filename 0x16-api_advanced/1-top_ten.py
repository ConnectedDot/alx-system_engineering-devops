#!/usr/bin/python3

"""This script queries the Reddit api and returns
the title of the first 10 hot post for a subreddit"""

import requests


def top_ten(subreddit):
    """Returns the titles of the top ten posts in a given subreddit."""
    if type(subreddit) is not str:
        return 0
    # Set up the request parameters
    url = "https://www.reddit.com/r/{}/hot/.json?".format(subreddit)
    params = {
        'limit': 10,
    }
    set_header = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}

    res = requests.get(url, headers=set_header, params=params)
    try:
        data = res.json()["data"]["children"]
        for title in data:
            print(title["data"]["title"])
    except Exception:
        print(None)