#!/usr/bin/python3
""" Module """

import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id), verify=False).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?user_id={}".
                        format(user_id), verify=False).json()
    completed_tasks = []
    for task in todos:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(url.get('name'), len(completed_tasks), len(todos)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
