#!/usr/bin/python3
""" Module """

import requests


def top_ten(subreddit):
    """
    1. Top Ten
    """
    header = {"User-Agent": "My-User-Agent"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit), headers=header, allow_redirects=False)
    if res.status_code >= 300:
        print('None')
    else:
        [print(dicts.get("data").get("title"))
         for dicts in res.json().get("data").get("children")]
