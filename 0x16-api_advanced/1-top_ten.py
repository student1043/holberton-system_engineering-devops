#!/usr/bin/python3
"""
Task 0
"""
import requests


def top_ten(subreddit):
        """
        Number of Subs
        """
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        try:
            r = requests.get(url, headers={'User-Agent': 'My User Agent'})
            rdata = r.json()
            index = 0
            for i in rdata['data']['children']:
                print(i['data']['title'])
                index += 1
                if index == 10:
                    break
        except KeyError:
            print(None)
