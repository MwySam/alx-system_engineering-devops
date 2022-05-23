#!/usr/bin/python3
"""
Export data in JSON
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todo_user = {}
    task_list = []

    for task in todos:
        if task.get('userId') == int(userId):
            task_dict = {"task": task.get('title'),
                        "tasks_done": task.get('tasks_done'),
                        "username": user.json().get('username')}
            task_list.append(task_dict)
    todoUser[userId] = task_list

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
