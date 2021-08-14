
from static_data.model_builder_statics import DJANGO_FIELDS, \
                                            DJANGO_RELATION_FIELDS, \
                                            DJANGO_ON_DELETE_ACTIONS

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
    print()
    show_models(models)

    print("- Create model ['c']")
    print("- Modify a model [enter an index of models]")
    print("- Export models.py ['e']")
    print("- Reset all models ['k']")
    print("- Quit ['q']")
    print()

def show_model_menu(model):
    print()
    print("model: {}\n".format(model.name))
    show_fields(model.fields)

    print("- Add field ['a']")
    print("- Delete a field [enter an index of fields]")
    print("- Delete model ['d']")
    print("- Rename model ['r']")
    print("- Print model ['p']")
    print("- Reset model ['k']")
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

def show_on_delete_actions():
	models_show_str = ""
	for (index, item) in enumerate(DJANGO_ON_DELETE_ACTIONS):
		models_show_str += "\t{}: {}\n".format(index ,repr(item))
	print("on delete: [\n{}]\n".format(models_show_str))
