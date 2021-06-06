#
# Django-modeler v0.2.3
# By Ray (__mr__)
#

import sys

from model_builder import *
from menu_module import *

MODELS = []
FIELD_PREFIX = False
PROMPT = "Enter a command: "

def main_menu():

    while True:
        show_main_menu(MODELS)

        user_input = input(PROMPT).lower()

        valid_inputs = ['c','e','q']

        MODELS_INDICES = map(str, range(len(MODELS)))

        valid_inputs.extend(MODELS_INDICES)

        if user_input in valid_inputs:
            return user_input

def main():
    try:
        print("\nDjango-Modeler (%s)" % VERSION)
        print("Written by Ray (__mr__)\n")
        command = main_menu()



    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(0)

if __name__ == '__main__':
    
    main()

