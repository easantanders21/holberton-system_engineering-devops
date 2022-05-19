#!/usr/bin/python3
""" Extend your Python script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ main """
    file_name = ("todo_all_employees.json")
    data = {}
    aux_dict = {}

    # Get information of the users and todos
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        data[user.get('id')] = []
        aux_dict[user.get('id')] = user.get('username')

    for todo in todos:
        task_dict = {}
        task_dict["task"] = todo.get('title')
        task_dict["completed"] = todo.get("completed")
        task_dict['username'] = aux_dict.get(todo.get('userId'))
        data.get(todo.get('userId')).append(task_dict)

    with open(file_name, mode="w") as jsonfile:
        json.dump(data, jsonfile)
