#
# Django-modeler v0.3.2
# By Ray (__mr__)
#

import sys
import os

from menu_module import *
from field_menu import *
from utility import *
from static_data.prompts import MAIN_PROMPT, \
                            CREATE_MODEL_NAME_PROMPT, \
                            ADD_FIELD_TYPE_PROMPT, \
                            ADD_FIELD_NAME_PROMPT
from static_data.meta import *

# Setting up colors for windows os
if os.name == 'nt':
    os.system("color")

MODELS = list()

def create_new_model():
    model_name = input(CREATE_MODEL_NAME_PROMPT)

    if not model_name: # If name isn't empty
        print("Model name should contain at least a character!")
        print("Aborted!\n")
        return False

    if validate_name(model_name) == False: # If name isn't validated return to main menu
        show_error()
        print("Model name should match Python3 naming conventions!")
        print("Aborted!\n")
        return False

    for item in MODELS:
        if model_name == item.name:
            show_error()
            print("This model is already created!")
            print("Aborted!\n")
            return False

    new_model = Model_Builder(model_name)
    print()
    show_success()
    print("Created model '{}'\n".format(model_name))

    MODELS.append(new_model)

def export_models():
    pass

def add_field():
    pass

def delete_model():
    pass

def show_model():
    pass

def delete_field():
    pass

def select_model(index):
    model = MODELS[index]
    valid_inputs = ['a','d','r','p','q']
    FIELDS_INDICES = map(str, range(len(model.fields)))
    valid_inputs.extend(FIELDS_INDICES)

    while True:
        show_model_menu(model)
        user_input = input(MAIN_PROMPT).lower()
        if user_input in valid_inputs:
            if user_input == 'a':   # add new field
                pass
            elif user_input == 'd': # delete model
                pass
            elif user_input == 'r': # rename model
                pass
            elif user_input == 'p': # show model
                pass
            elif user_input == 'q': # return to main menu
                return
            else:                   # delete field
                pass

def main_menu():
    valid_inputs = ['c', 'e', 'q']
    MODELS_INDICES = map(str, range(len(MODELS)))
    valid_inputs.extend(MODELS_INDICES)

    while True:
        show_main_menu(MODELS)
        user_input = input(MAIN_PROMPT).lower()

        if user_input in valid_inputs:
            if user_input == 'c':   # create new model
                create_new_model()
            elif user_input == 'e': # export models.py
                pass
            elif user_input == 'q': # exit from main_menu
                return
            else:                   # selecting models
                pass

if __name__ == '__main__':
    print(BANNER)
    try:
        main_menu()

    except KeyboardInterrupt:
        pass

    print("\nBye")
