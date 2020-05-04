#!/usr/bin/python3
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
    for i in userdata:
        name = i['name']
    for i in rdata:
        if i['completed']:
            total += 1
            done += 1
        else:
            total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for titles in rdata:
        if titles['completed']:
            print("\t {}".format(titles['title']))
