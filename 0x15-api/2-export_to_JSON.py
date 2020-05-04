#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}".
                        format(sys.argv[1]))
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                     format(sys.argv[1]))
    userdata = user.json()
    rdata = r.json()
    total = 0
    done = 0
    mytitles = []
    for i in userdata:
        name = i['name']
        username = i['username']
    for i in rdata:
        if i['completed']:
            total += 1
            done += 1
        else:
            total += 1
    for titles in rdata:
        if titles['completed']:
            mytitles.append(titles['title'])
    with open("{}.json".format(sys.argv[1]), "w+") as f:
            f.write("{")
            f.write('"{}": ['.format(sys.argv[1]))
            for elem in rdata:
                f.write(json.dumps({'task': elem["title"],
                                    'completed': elem["completed"],
                                    'username': username}))
                f.write(", ")
            f.write("}]")
