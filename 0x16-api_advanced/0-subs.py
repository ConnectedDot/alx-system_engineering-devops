#!/usr/bin/python3


"""This script queries the Reddit API and returns
the number of total subcribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if type(subreddit) is not str:
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)

    response = requests.get(url, headers=user_agent)
    try:
        return (response.json()["data"]["subscribers"])
    except Exception:
        return 0