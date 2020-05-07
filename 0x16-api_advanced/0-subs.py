#!/usr/bin/python3
import requests
import json


def number_of_subscribers(subreddit):
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        r = requests.get(url, headers={'User-Agent': 'My User Agent'})
        rdata = r.json()
        a = json.loads(r.text)
        if(a['kind'] == 'Listing'):
            return 0
        else:
            return(rdata['data']['subscribers'])
