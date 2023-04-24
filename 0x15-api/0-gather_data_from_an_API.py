#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    users_todo = requests.get(url + "users_todo", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in users_todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(users_todo)))
    [print("\t {}".format(c)) for c in completed]