#!/usr/bin/python3
"""
Gather data from API
"""
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    user_name = user.json().get('user_name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    tasks_done = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            total_tasks += 1
            if task.get('completed'):
                tasks_done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, tasks_done, total_tasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
