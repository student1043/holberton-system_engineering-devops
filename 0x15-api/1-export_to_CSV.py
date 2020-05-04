#!/usr/bin/python3
import requests
import csv
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
    with open("{}.csv".format(sys.argv[1]), "w+") as myfile:
            f = csv.writer(myfile, delimiter=",",
                           quoting=csv.QUOTE_ALL)
            for elem in rdata:
                f.writerow([elem["userId"], username, elem["completed"],
                            elem["title"]])
