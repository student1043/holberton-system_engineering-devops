#!/usr/bin/python3
"""
Task 0
"""
import json
import requests


def number_of_subscribers(subreddit):
        """
        Number of Subs
        """
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        r = requests.get(url, headers={'User-Agent': 'My User Agent'})
        rdata = r.json()
        a = json.loads(r.text)
        if(a['kind'] == 'Listing'):
            return 0
        else:
            return(rdata['data']['subscribers'])
