#!/usr/bin/python3
""" Script that uses a REST API """
import requests
from sys import argv
import json


if __name__ == "__main__":
    """ main """
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    # Get information of user
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        if user['id'] == int(argv[1]):
            EMPLOYEE_NAME = user['name']
            break

    # Get information todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for todo in todos:
        if todo['userId'] == int(argv[1]):
            if todo['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))

    for quote in TASK_TITLE:
        print("\t {}".format(quote))
