#!/usr/bin/python3
""" Module """

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    1. Top Ten
    """
    settings = {"count": count, "after": after}
    header = {"User-Agent": "My-User-Agent"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers=header, allow_redirects=False, settings)
    if res.status_code >= 400:
        return None

    lis = hot_list + [dicts.get("data").get("title")
                        for dicts in res.json()
                        .get("data")
                        .get("children")]

    sett = res.json()
    if not sett.get("data").get("after"):
        return lis

    return recurse(subreddit, lis, sett.get("data").get("count"),
                   sett.get("data").get("after"))
