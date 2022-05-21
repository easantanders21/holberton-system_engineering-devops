#!/usr/bin/python3
"""  function that queries the Reddit API;
and print ten titles """
import requests
import json


def count_words(subreddit, word_list):
    """ count words """
    try:
        list_T = []
        my_dict = {}
        hot_list = recurse(subreddit, list_T)
        str_word = " ".join(word_list).lower()
        word_list = str_word.split()
        str_list = " ".join(hot_list).lower()
        list_values = []
        recurse_3(my_dict, str_list, word_list, 0, list_values)
        print(my_dict)
    except Exception:
        print("fail")
        pass


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

def recurse_3(my_dict, str_list, word_list, i, list_values):
    try:
        n = 0
        my_word = word_list[i]
        n = str_list.count(my_word)
        if n > 0:
            #my_dict[my_word] = n
            list_values.append(n)
        i += 1
        #print(i)
        recurse_3(my_dict, str_list, word_list, i, list_values)
        #print(my_dict)
        print(n)
        print(my_word)
        print(list_values)
        if list_values[0] is n:
            print("{}: {}".format(my_word, n))
            list_values.pop(0)
        #    print("{}: {}".format(my_word, my_dict[my_word]))
    except Exception:
        #list_values = list(my_dict.values())
        list_values.sort(reverse=True)
        #print(list_values)
        return
