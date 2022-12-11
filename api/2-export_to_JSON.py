#!/usr/bin/python3
""" Api """

if __name__ == "__main__":
    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    t_url = ("https://jsonplaceholder.typicode.com/users/{}/todos"
             .format(userId))
    name = requests.get(user).json()
    todos = requests.get(t_url).json()

    with open('{}.json'.format(userId), 'w') as json_file:
        tasks = []
        for t in todos:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": name.get("username")})

        data = {"{}".format(userId): tasks}
        json.dump(data, json_file)
