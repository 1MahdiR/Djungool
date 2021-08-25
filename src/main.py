#
# Django-modeler v0.9.9
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
IMPORT_OPTIONS = list()

def create_new_model():
    model_name = input(CREATE_MODEL_NAME_PROMPT)

    if not model_name: # If name isn't empty
        show_error()
        print("Model name should contain at least a character!")
        print("Aborted!\n")
        print_seperator()
        return False

    if validate_name(model_name) == False: # If name isn't validated return to main menu
        show_error()
        print("Model name should match Python3 naming conventions!")
        print("Aborted!\n")
        print_seperator()
        return False

    for item in MODELS:
        if model_name == item.name:
            show_error()
            print("This model is already created!")
            print("Aborted!\n")
            print_seperator()
            return False

    new_model = Model_Builder(model_name)
    print()
    show_success()
    print("Created model '{}'\n".format(model_name))
    print_seperator()

    MODELS.append(new_model)

    select_model(-1) # selecting the last model that was added

def export_models():
    if os.path.isfile('models.py'):
        user_input = input(MODELS_PY_ALREADY_EXIST_PROMPT)
        if user_input.lower() != 'y':
            print("Aborted!\n")
            return
    else:
        show_error()
        print("'models.py' is not a regular file!")
        print("Aborted!\n")
        print_seperator()

    try:
        with open('models.py', 'w') as file:
            file.write("from django.db import models\n\n")
            for model in MODELS:
                file.write(str(model))
                file.write("\n")

        show_success()
        print("Models exported to 'models.py'.")
        print_seperator()

    except PermissionError:
        show_error()
        print("Permission error! You do not have the permission to write a file.")
        print("Aborted!\n")
        print_seperator()

def remove_all_models():
    print()
    show_warning()
    reply = input(RESET_ALL_MODELS_PROMPT)
    if reply.lower() != 'y':
        return
    for i in range(len(MODELS)):
        del(MODELS[0])

    print()
    show_success()
    print("Reset was successful\n")
    print_seperator()

def add_field(model):
    show_field_types()

    # choosing field type
    user_input = input(ADD_FIELD_TYPE_PROMPT)

    if not user_input:
        show_error()
        print("Empty input!")
        print("Aborted!\n")
        print_seperator()
        return False

    if not validate_field_type_input(user_input):
        show_error()
        print("Wrong input for index type field!")
        print("Aborted!\n")
        print_seperator()
        return False

    field_type = user_input

    # choosing field name
    user_input = input(ADD_FIELD_NAME_PROMPT)

    if not user_input:
        show_error()
        print("Field name should contain at least a character!")
        print("Aborted!\n")
        print_seperator()
        return False

    if validate_name(user_input) == False:
        show_error()
        print("Field name should match Python3 naming conventions!")
        print("Aborted!\n")
        print_seperator()
        return False

    for item in model.fields:
        if user_input == item.get_name():
            show_error()
            print("This field is already created!")
            print("Aborted!\n")
            print_seperator()
            return False

    name = user_input
    field = None

    if field_type == '0': #BigIntegerField_client
        field = BigIntegerField_client(name)
    elif field_type == '1': #BooleanField_client
        field = BooleanField_client(name)
    elif field_type == '2': #CharField_client
        try:
            field = CharField_client(name)
        except ValueError as e:
            show_error()
            print(e)
            print_seperator()
            return
    elif field_type == '3': #DateField_client
        field = DateField_client(name)
    elif field_type == '4': #DateTimeField_client
        field = DateTimeField_client(name)
    elif field_type == '5': #DecimalField_client
        field = DecimalField_client(name)
    elif field_type == '6': #EmailField_client
        field = EmailField_client(name)
    elif field_type == '7': #FileField_client
        field = FileField_client(name)
    elif field_type == '8': #FloatField_client
        field = FloatField_client(name)
    elif field_type == '9': #ImageField_client
        field = ImageField_client(name)
    elif field_type == '10': #IntegerField_client
        field = IntegerField_client(name)
    elif field_type == '11': #PositiveBigIntegerField_client
        field = PositiveBigIntegerField_client(name)
    elif field_type == '12': #PositiveIntegerField_client
        field = PositiveIntegerField_client(name)
    elif field_type == '13': #PositiveSmallIntegerField_client
        field = PositiveSmallIntegerField_client(name)
    elif field_type == '14': #SlugField_client
        field = SlugField_client(name)
    elif field_type == '15': #SmallIntegerField_client
        field = SmallIntegerField_client(name)
    elif field_type == '16': #TextField_client
        field = TextField_client(name)
    elif field_type == '17': #TimeField_client
        field = TimeField_client(name)
    elif field_type == '18': #URLField_client
        field = URLField_client(name)
    elif field_type == '19': #UUIDField_client
        field = UUIDField_client(name)
    elif field_type == '20': #ForeignKey_client
        try:
            field = ForeignKey_client(name)
        except (IndexError, ValueError) as e:
            show_error()
            print(e)
            print_seperator()
            return
    elif field_type == '21':
        try:
            field = ForeignKey_client(name)
        except (IndexError, ValueError) as e:
            show_error()
            print(e)
            print_seperator()
            return
    elif field_type == '22':
        try:
            field = ForeignKey_client(name)
        except (IndexError, ValueError) as e:
            show_error()
            print(e)
            print_seperator()
            return

    if field:
        model.add_field(field)

    print()
    show_success()
    print("New field '{}' has been added!\n".format(name))
    print_seperator()

def delete_model(model):
    try:
        print("\n",model,"\n",sep="")
        show_warning()
        reply = input(MODEL_DELETE_CONFIRMATION_PROMPT)
        if reply.lower() != 'y':
            return
        MODELS.remove(model)

        print()
        show_success()
        print("Model '{}' has been deleted!\n".format(model.name))
        print_seperator()

        return True # return to main menu

    except ValueError:
        pass

def rename_model(model):
    model_name = input(CREATE_MODEL_NAME_PROMPT)

    if not model_name: # If name isn't empty
        show_error()
        print("Model name should contain at least a character!")
        print("Aborted!\n")
        print_seperator()
        return False

    if validate_name(model_name) == False: # If name isn't validated return to main menu
        show_error()
        print("Model name should match Python3 naming conventions!")
        print("Aborted!\n")
        print_seperator()
        return False

    for item in MODELS:
        if model_name == item.name:
            show_error()
            print("This model is already created!")
            print("Aborted!\n")
            print_seperator()
            return False

    model.name = model_name
    print()
    show_success()
    print("Renamed model to '{}'\n".format(model_name))
    print_seperator()

def show_model(model):
    print()
    print_seperator()
    print('\n')
    print(model)
    print_seperator()
    print('\n')
    input()

def remove_all_fields(model):
    print()
    show_warning()
    reply = input(RESET_ALL_FIELDS_PROMPT)
    if reply.lower() != 'y':
        return
    for i in range(len(model.fields)):
        model.remove_field(0)

    print()
    show_success()
    print("Reset was successful\n")
    print_seperator()

def delete_field(model, index):
    try:
        field = model.get_field(index)
        print("\n",field,"\n",sep="")
        show_warning()
        reply = input(FIELD_DELETE_CONFIRMATION_PROMPT)
        if reply.lower() != 'y':
            return
        model.remove_field(index)

        print()
        show_success()
        print("Field '{}' has been deleted!\n".format(field.get_name()))
        print_seperator()

    except IndexError:
        pass

def select_model(index):
    try:
        model = MODELS[index]
    except IndexError:
        return

    valid_inputs = ['a','d','r','p','q','k']

    while True:
        FIELDS_INDICES = map(str, range(len(model.fields)))
        valid_inputs.extend(FIELDS_INDICES)

        show_model_menu(model)
        user_input = input(MAIN_PROMPT).lower()
        if user_input in valid_inputs:
            try:
                if user_input == 'a':   # add new field
                    add_field(model)
                elif user_input == 'd': # delete model
                    if delete_model(model):
                        return
                elif user_input == 'r': # rename model
                    rename_model(model)
                elif user_input == 'p': # show model
                    show_model(model)
                elif user_input == 'k':
                    remove_all_fields(model)
                elif user_input == 'q': # return to main menu
                    return
                else:                   # delete field
                    if user_input.isdigit():
                        index = int(user_input)
                        delete_field(model, index)

            except KeyboardInterrupt:
                print("\nAborted!\n")

def main_menu():
    valid_inputs = ['c', 'e', 'q', 'k']

    while True:
        MODELS_INDICES = map(str, range(len(MODELS)))
        valid_inputs.extend(MODELS_INDICES)

        show_main_menu(MODELS)
        user_input = input(MAIN_PROMPT).lower()

        if user_input in valid_inputs:
            if user_input == 'c':   # create new model
                create_new_model()
            elif user_input == 'e': # export models.py
                export_models()
            elif user_input == 'k': # reset everything
                remove_all_models()
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
