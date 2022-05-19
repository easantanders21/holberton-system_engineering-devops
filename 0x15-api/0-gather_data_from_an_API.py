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
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    user = requests.get(url).json()
    EMPLOYEE_NAME = user['name']

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
