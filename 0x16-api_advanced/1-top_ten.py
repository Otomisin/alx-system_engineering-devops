#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dictn = response.json()
    hot_post = dictn['data']['children']
    if len(hot_post) is 0:
        print(None)
    else:
        for post in hot_post:
            print(post['data']['title'])