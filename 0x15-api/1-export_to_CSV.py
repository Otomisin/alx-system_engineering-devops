#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import json
import sys
from urllib import request, parse

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = json.loads(request.urlopen(f"{url}users/{user_id}").read())
    username = user.get("username")
    user_todos = json.loads(
        request.urlopen(f"{url}todos?
                        {parse.urlencode({'userId': user_id})}").read())

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in user_todos:
            writer.writerow([user_id,
                             username, todo.get("completed"),
                             todo.get("title")])
