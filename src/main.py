#
# Django-modeler v0.2.3
# By Ray (__mr__)
#

import sys
import os

from model_builder import *
from menu_module import *
from field_menu import *

if os.name == 'nt':
    os.system("color")

MODELS = []
FIELD_PREFIX = False
MAIN_PROMPT = "Enter a command: "
CREATE_MODEL_NAME_PROMPT = "Enter a name for model: "
ADD_FIELD_TYPE_PROMPT = "Enter a type [0-22]: "
ADD_FIELD_NAME_PROMPT = "Enter a name for field: "

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

def validate_field_type_input(user_input):
    return user_input.isdigit() and 0 <= int(user_input) <= 21

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

def add_field_menu(model):

    show_add_field_menu()

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
                    model = MODELS[-1]
                    command = modify_model_menu(MODELS[-1], len(MODELS)-1)

                    if command == 'q':
                        break

                    if command == 'a':
                        add_field_menu(model)



            elif command == 'q':
                break

        print('Bye!')
        sys.exit(0)

    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(0)

if __name__ == '__main__':

    main()
