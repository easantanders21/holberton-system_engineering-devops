#!/usr/bin/python3
"""  function that queries the Reddit API;
and print ten titles """
import requests


def top_ten(subreddit):
    """ return number of subscriebers """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json().get("data")
        list_children = response.get("children")
        for childrens in list_children:
            print(childrens.get("data").get("title"))
    except Exception:
        print("None")
