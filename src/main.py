#
# Django-modeler v0.2.3
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

def main_menu():
    valid_inputs = ['c', 'e', 'q']
    MODELS_INDICES = map(str, range(len(MODELS)))
    valid_inputs.extend(MODELS_INDICES)

    while True:
        show_main_menu(MODELS)
        user_input = input(MAIN_PROMPT).lower()

        if user_input in valid_inputs:
            if user_input == 'c': # create new model
                pass
            elif user_input == 'e': # export models.py
                pass
            elif user_input == 'q': # exit from main_menu
                return
            else: # selecting models
                pass

if __name__ == '__main__':
    print(BANNER)
    try:
        main_menu()

    except KeyboardInterrupt:
        pass

    print("\nBye")
