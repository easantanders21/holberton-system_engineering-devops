#!/usr/bin/python3
"""  function that queries the Reddit API;
and print ten titles """
import requests
import json


def recurse(subreddit, hot_list=[]):
    """ return list of title """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        response = requests.get(url, header,
                                allow_redirects=False).json().get(
                                    "data").get("children")
        recurse_2(0, response, hot_list)
        return(hot_list)
    except Exception:
        return(None)


def recurse_2(children_i=0, children_list=[], hot_list=[]):
    """ recurse function """
    try:
        hot_list.append(children_list[children_i].get("data").get("title"))
        children_i += 1
        recurse_2(children_i, children_list, hot_list)
    except Exception:
        return
