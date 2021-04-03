#!/usr/bin/python3
"""
0. Gather data from an API
"""
import requests
from sys import agrv

if __name__ == "__main__":

    user_1 = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user1))
    response = requests.get("{}/{}".format(url, user_1), verify=False)
    if response.status_code == 200:
        tasks = []
        total_tasks = 0
        completed = 0
        content = response.json()
        todos = requests.get('https://jsonplaceholder.typicode.com/todos')
        todos = todos.json()
        total_tasks = len(todos)
        for task in todos:
            if task.get('user_1') == int(user_1):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('user_1') == int(user_1) and task.get('completed')]))
