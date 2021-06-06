
from model_builder import DJANGO_FIELDS, \
                          DJANGO_RELATION_FIELDS, \
                          DJANGO_ON_DELETE_ACTIONS

VERSION = "v0.2.3"

def show_models(models):
    if models:
        models_show_str = ""
        for (index, item) in enumerate(models):
            models_show_str += "\t{}: {}\n".format(index ,repr(item))
        print("models: [\n{}]\n".format(models_show_str))
    else:
        print("models: [\n\tStill no model\n]\n")

def show_fields(fields):
    if fields:
        fields_show_str = ""
        for (index, item) in enumerate(fields):
            fields_show_str += "\t{}: {}\n".format(index, repr(item))
        print("fields: [\n{}]\n".format(fields_show_str))
    else:
        print("fields: [\n\tStill no field\n]\n")

def show_main_menu(models):
    show_models(models)

    print("- Create model ['c']")
    print("- Modify a model [enter an index of models]")
    print("- Export model.py ['e']")
    print("- Quit ['q']")
    print()

def show_model_menu(model):
    print("model: {}\n".format(model.name))
    show_fields(model.fields)

    print("- Add field ['a']")
    print("- Delete a field [enter an index of fields]")
    print("- Delete model ['d']")
    print("- Rename model ['r']")
    print("- Return from model menu ['q']")
    print()
    
def show_field_types():
    items = list()
    items.extend(DJANGO_FIELDS)
    items.extend(DJANGO_RELATION_FIELDS)
    
    types_show_str = ""

    for (index, item) in enumerate(items):
        types_show_str += "\t{}: {}\n".format(index, item)

    print("field type: [\n{}]\n".format(types_show_str))

