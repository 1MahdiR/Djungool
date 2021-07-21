
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
    
