
VERSION = "v0.1.2"

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
    print("\nDjango-Modeler (%s)" % VERSION)
    print("Written by Ray (__mr__)\n")
    show_models(models)

    print("- Create model ['c']")
    print("- Modify a model [enter an index of models]")
    print("- Export model.py ['e']")
    print("- Quit ['q']")
    print()

def show_model_menu(model):
    print("\nmodel: {}\n".format(model.name))
    show_fields(model.fields)

    print("- Add field ['a']")
    print("- Delete a field [enter an index of fields]")
    print("- Delete model ['d']")
    print("- Rename model ['r']")
    print("- Return from model menu ['q']")
    print()
    