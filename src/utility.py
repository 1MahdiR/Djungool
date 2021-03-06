from re import compile as re_compile
from keyword import kwlist as keywords

from static_data.model_builder_statics import DJANGO_FIELDS, \
                                        DJANGO_RELATION_FIELDS

def show_error():
    print("\033[1;31mError:\033[0;0m ", end="")

def show_success():
    print("\033[1;32mSuccess:\033[0;0m ", end="")

def show_warning():
    print("\033[1;33mWarning:\033[0;0m ", end="")

def print_seperator():
    print("\033[1;32m" + ('*' * 32) + "\033[0;0m ", end="")

def print_in_box(message):
    length = len(message)
    print("╔", ("═" * (length + 2)), "╗", sep="")
    print("║", message, "║")
    print("╚", ("═" * (length + 2)), "╝", sep="")

def validate_name(name):
    if name in keywords: return False # If name was a Python3 keyword returns False

    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

    for i in name:
        if i not in valid_letters:
            return False

    return False if name[0].isdigit() else True

def validate_field_type_input(user_input):
    length = len(DJANGO_FIELDS) + len(DJANGO_RELATION_FIELDS) - 1
    return user_input.isdigit() and 0 <= int(user_input) <= length

def validate_path(path):
    pattern = re_compile("^[a-z0-9-_]+(/[a-z0-9-_]+)*/$") # finds relative paths: "aaa/bbb/ccc/"

    if pattern.search(path):
        return True
    else:
        return False

def validate_integer(number):
    pattern = re_compile("^-?[0-9]+$")

    if pattern.search(number):
        return True
    else:
        return False
