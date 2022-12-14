#!/usr/bin/env python3

"""
Name: cappdata.py
Purpose: component lists and query function for use with
           django-repocapp.py and associated scripts

source: https://gitlab.com/kevinbowen/django-repocapp
version: 0.1.0
updated: 20220922
@author: kevin.bowen@gmail.com
"""

import sys
import termios
import tty


def component_list(component_group_list):
    """returns lists of components."""
    if component_group_list == "django":
        django = [
            "bookstore",
            "cheese",
            "django-todo",
            "django-blog",
            "django-polls",
            "django-start",
            "learning-log",
            "library",
            "message-board",
            "news",
            "superlists",
        ]
        return django


    elif component_group_list == "djangorestframework":
        djangorestframework = {
            "django-api-blog",
            "django-api-library",
            "django-api-todo",
            "djapi-blog",
            "djapi-library",
            "djapi-todo",
            "pastebin-drf-api",
        }
        return djangorestframework


    elif component_group_list == "flask":
        flask = {
            "flaskblog",
            "flask-chat",
        }
        return flask


    elif component_group_list == "fastapi":
        fastapi = {
            "recipes",
        }
        return fastapi


    elif component_group_list == "all_components":
        all_components = {
            "django": "django",
            "djangorestframework": "djangorestframework",
            "flask": "flask",
            "fastapi": "fastapi",
        }
        return all_components

    else:
        return None


def press_any_key():
    """Doesn't work for shift/control keys."""
    file_descriptor = sys.stdin.fileno()
    tty_attributes = termios.tcgetattr(file_descriptor)
    try:
        print("Press any to continue...")
        tty.setraw(file_descriptor)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, tty_attributes)


def query_yes_no(question, answer="no"):
    """
    Handles confirmation prompts. Used in install_xfce.py
    and purge_xfce.py
    """
    valid = {"yes": "yes", "y": "yes", "no": "no", "n": "no"}
    prompt = " [(Y)es/(N)o/Default: No] "

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        try:
            if answer is not None and choice == "":
                return answer
            elif answer in valid:
                return valid[choice]
        except KeyError:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n"
            )


if __name__ == "__main__":
    pass
