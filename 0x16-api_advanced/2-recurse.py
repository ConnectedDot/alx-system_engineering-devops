#!/usr/bin/python3

"""This script is queries the reddit API and returns
a list of all hot posts"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """list of all hot titles for a subreddit"""
    if type(subreddit) is not str:
        return None
    global after
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    set_header = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}
    pagination = {"after": after}

    res = requests.get(url, headers=set_header, params=pagination)
    try:
        get_after = res.json()["data"]["after"]
        if get_after is not None:
            after = get_after
            recurse(subreddit, hot_list)
        data = res.json()["data"]["children"]
        for title in data:
            hot_list.append(title["data"]["title"])
        return hot_list
    except Exception:
        return None