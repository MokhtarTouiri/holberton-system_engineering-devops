#!/usr/bin/python3
""" Module """

import requests


def number_of_subscribers(subreddit):
    """
    0. How many subs?
    """
    header = {"User-Agent": "My-User-Agent"}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers=header, allow_redirects=False)
    if res.status_code >= 300:
        return 0

    return res.json().get("data").get("subscribers")
