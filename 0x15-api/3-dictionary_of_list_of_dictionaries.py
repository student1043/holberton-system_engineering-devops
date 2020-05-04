#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    userdata = user.json()
    rdata = r.json()
    mydic = dict()
    for i in range(1, len(userdata) + 1):
        usersid = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(i))
        usersinfo = requests.get(
                    "https://jsonplaceholder.typicode.com/users/{}"
                    .format(i))
        username = usersinfo.json()['username']
        info = usersid.json()
        mydic[str(i)] = []
        for j in info:
            elements = dict()
            elements["username"] = username
            elements["task"] = j.get("title")
            elements["completed"] = j.get("completed")
            mydic[str(i)].append(elements)
        with open("todo_all_employees.json", "w+", newline="") as f:
            json.dump(mydic, f)
