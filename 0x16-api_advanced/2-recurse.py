#!/usr/bin/python3
"""
Task 0
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
        """
        Number of Subs
        """
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        try:
            r = requests.get(url, headers={'User-Agent': 'My User Agent'},
                             params={'after': after})
            rdata = r.json()
            after = rdata['data']['after']
            for i in rdata['data']['children']:
                hot_list.append(i['data']['title'])
        except KeyError or AttributeError:
            return None
        if after:
            recurse(subreddit, hot_list, after)
        if len(hot_list) > 0:
            return hot_list
        else:
            return None

