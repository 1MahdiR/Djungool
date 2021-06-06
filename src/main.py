#
# Django-modeler v0.2.3
# By Ray (__mr__)
#

import sys

from model_builder import *
from menu_module import *

MODELS = []
FIELD_PREFIX = False
MAIN_PROMPT = "Enter a command: "
CREATE_MODEL_NAME_PROMPT = "Enter a name for model: "

def validate_name(name):
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    
    for i in name:
        if i not in valid_letters:
            return False

    return False if name[0].isdigit() else True

def main_menu():

    while True:
        show_main_menu(MODELS)

        user_input = input(MAIN_PROMPT).lower()

        valid_inputs = ['c','e','q']

        MODELS_INDICES = map(str, range(len(MODELS)))

        valid_inputs.extend(MODELS_INDICES)

        if user_input in valid_inputs:
            return user_input

def create_model_menu():
        
    model_name = input(CREATE_MODEL_NAME_PROMPT)

    if not model_name: # If name isn't empty
        print("Model name should contain at least a character!")
        print("Aborted!\n")
        return

    if validate_name(model_name) == False: # If name isn't validated return to main menu
        print("Model name should match Python3 naming conventions!")
        print("Aborted!\n")
        return

    print()

def main():
    try:
        print("\nDjango-Modeler (%s)" % VERSION)
        print("Written by Ray (__mr__)\n")
        while True:
            command = main_menu()
            print()

            if command == 'c': # Create model
                create_model_menu()



    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(0)

if __name__ == '__main__':
    
    main()

