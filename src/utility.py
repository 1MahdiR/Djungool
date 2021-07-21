from static_data.model_builder_statics import DJANGO_FIELDS, \
                                        DJANGO_RELATION_FIELDS

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
    length = len(DJANGO_FIELDS) + len(DJANGO_RELATION_FIELDS) - 1
    return user_input.isdigit() and 0 <= int(user_input) <= length
