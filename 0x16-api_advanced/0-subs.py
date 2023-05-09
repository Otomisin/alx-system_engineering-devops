#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of
    subscribers for a given subreddit """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dictn = res.json()
    if 'data' not in dictn:
        return 0
    if 'subscribers' not in dictn.get('data'):
        return 0
    return res.json()['data']['subscribers']
