#!/usr/bin/python3
"""
Task 0
"""
import requests


def number_of_subscribers(subreddit):
        """
        Number of Subs
        """
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        try:
            r = requests.get(url, headers={'User-Agent': 'My User Agent'})
            rdata = r.json()
            return(rdata['data']['subscribers'])
        except KeyError:
            return 0
