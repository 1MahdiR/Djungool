#
# Django-modeler v0.4.7
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

    select_model(-1) # selecting the last model that was added

def export_models():
    pass

def add_field(model):
    show_field_types()

    # choosing field type
    user_input = input(ADD_FIELD_TYPE_PROMPT)

    if not user_input:
        show_error()
        print("Empty input!")
        print("Aborted!\n")
        return False

    if not validate_field_type_input(user_input):
        show_error()
        print("Wrong input for index type field!")
        print("Aborted!\n")
        return False

    field_type = user_input

    # choosing field name
    user_input = input(ADD_FIELD_NAME_PROMPT)

    if not user_input:
        show_error()
        print("Field name should contain at least a character!")
        print("Aborted!\n")
        return False

    if validate_name(user_input) == False:
        show_error()
        print("Field name should match Python3 naming conventions!")
        print("Aborted!\n")
        return False

    name = user_input
    field = None

    if field_type == '0':
        field = BigIntegerField_client(name)
    elif field_type == '1':
        field = BooleanField_client(name)
    elif field_type == '2':
        field = CharField_client(name)
    elif field_type == '3':
        field = DateField_client(name)
    elif field_type == '4':
        field = DateTimeField_client(name)
    elif field_type == '5':
        field = DecimalField_client(name)
    elif field_type == '6':
        field = EmailField_client(name)
    elif field_type == '7':
        field = FileField_client(name)
    elif field_type == '8':
        field = FloatField_client(name)
    elif field_type == '9':
        field = ImageField_client(name)
    elif field_type == '10':
        field = IntegerField_client(name)
    elif field_type == '11':
        field = PositiveBigIntegerField_client(name)
    elif field_type == '12':
        field = PositiveIntegerField_client(name)
    elif field_type == '13':
        field = PositiveSmallIntegerField_client(name)
    elif field_type == '14':
        field = SlugField_client(name)
    elif field_type == '15':
        field = SmallIntegerField_client(name)
    elif field_type == '16':
        field = TextField_client(name)
    elif field_type == '17':
        field = URLField_client(name)
    elif field_type == '18':
        field = UUIDField_client(name)
    elif field_type == '19':
        field = UUIDField_client(name)
    elif field_type == '20':
        field = ForeignKey_client(name)
    elif field_type == '21':
        field = ManyToManyField_client(name)
    elif field_type == '22':
        field = OneToOneField_client(name)

    model.add_field(field)

def delete_model(model):
    MODELS.remove(model)

def rename_model(model):
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

    model.name = model_name
    print()
    show_success()
    print("Renamed model to '{}'\n".format(model_name))

def show_model(model):
    print()
    print("*" * 32, end="\n\n")
    print(model)
    print("*" * 32, end="\n\n")

def delete_field():
    pass

def select_model(index):
    try:
        model = MODELS[index]
    except IndexError:
        return

    valid_inputs = ['a','d','r','p','q']

    while True:
        FIELDS_INDICES = map(str, range(len(model.fields)))
        valid_inputs.extend(FIELDS_INDICES)

        show_model_menu(model)
        user_input = input(MAIN_PROMPT).lower()
        if user_input in valid_inputs:
            if user_input == 'a':   # add new field
                add_field(model)
            elif user_input == 'd': # delete model
                delete_model(model)
                return
            elif user_input == 'r': # rename model
                rename_model(model)
            elif user_input == 'p': # show model
                show_model(model)
            elif user_input == 'q': # return to main menu
                return
            else:                   # delete field
                pass

def main_menu():
    valid_inputs = ['c', 'e', 'q']

    while True:
        MODELS_INDICES = map(str, range(len(MODELS)))
        valid_inputs.extend(MODELS_INDICES)

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
                select_model(int(user_input))

if __name__ == '__main__':
    print(BANNER)
    try:
        main_menu()

    except KeyboardInterrupt:
        pass

    print("\nBye")
