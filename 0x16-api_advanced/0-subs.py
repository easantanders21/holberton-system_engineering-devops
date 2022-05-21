#!/usr/bin/python3
"""  function that queries the Reddit API;
and returns the number of subscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscriebers """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, header,
                                allow_redirects=False).json().get("data")
        return(response.get("subscribers"))
    except Exception:
        return(0)
