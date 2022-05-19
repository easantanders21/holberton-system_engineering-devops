#!/usr/bin/python3
""" Extend your Python script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ main """
    file_name = "{}.json".format(argv[1])
    user_id = int(argv[1])
    data = {user_id: []}
    aux_dict = {}

    # Get information of the users and todos
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1])).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                argv[1])).json()

    for todo in todos:
        aux_dict["task"] = todo.get("title")
        aux_dict["completed"] = todo.get("completed")
        aux_dict["username"] = users.get("username")
        data[user_id].append(aux_dict)
        aux_dict = {}

    with open(file_name, mode="w") as jsonfile:
        json.dump(data, jsonfile)
