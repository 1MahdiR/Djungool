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

def show_error():
    print("\033[1;31mError:\033[0;0m ", end="")

def show_success():
    print("\033[1;32mSuccess:\033[0;0m ", end="")

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

def modify_model_menu(model, index):

    while True:
        show_model_menu(model)

        user_input = input(MAIN_PROMPT).lower()

        valid_inputs = ['a','d','r','q']

        FIELDS_INDICES = map(str, range(len(model.fields)))

        valid_inputs.extend(FIELDS_INDICES)

        if user_input in valid_inputs:
            return user_input

def create_model_menu():
        
    model_name = input(CREATE_MODEL_NAME_PROMPT)

    if not model_name: # If name isn't empty
        show_error()
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

def main():
    try:
        print("\nDjango-Modeler (%s)" % VERSION)
        print("Written by Ray (__mr__)\n")
        while True:
            command = main_menu()
            print()

            if command == 'c': # Create model
                
                failed = create_model_menu()
                if failed == False:
                    continue
                
                while True:
                    command = modify_model_menu(MODELS[-1], len(MODELS)-1)
                    
                    if command == 'q':
                        break


                
            elif command == 'q':
                break

        print('Bye!')
        sys.exit(0)

    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(0)

if __name__ == '__main__':
    
    main()

