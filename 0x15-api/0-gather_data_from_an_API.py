#!/usr/bin/python3
"""
Gather data from API
"""

import requests
import sys


if __name__ == '__main__':

    user_id = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
            .format(user_id))

    user_name = user.json().get('user_name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    tasks_done = 0
    total_tasks = 0
    
    for task in todos.json():
        if task.get("user_id") == (user_id):
            total_tasks += 1
            if task.get("tasks_done"):
            tasks_done += 1

print(
   "Employee {} is done with tasks ({}/{}):"
    .format(user_name,tasks_done,total_tasks)
       
    "/t {}".format(tasks_done.get('title'))
    )
