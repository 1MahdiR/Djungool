from static_data.model_builder_statics import DJANGO_FIELDS, DJANGO_RELATION_FIELDS

# field_menu prompts
ENTER_DEFAULT_VALUE_PROMPT = "Enter a default value (enter nothing for no default): "
ENTER_CHOICES_OPTION_CONFIRM_PROMPT = "Add choices option? (y/N): "
ENTER_CHOICE_VALUE_PROMPT = "Enter the value of option (enter nothing to continue): "
ENTER_CHOICE_REPR_PROPMT = "Enter the human-readable name of option: "
ENTER_MAX_LENGTH_PROMPT = "Enter a value for max length ({}): "
ENTER_MAX_DIGIT_PROMPT = "Enter a value for max digit ({}): "
ENTER_DECIMAL_PLACES_PROMPT = "Enter a value for decimal places ({}): "
ENTER_UPLOAD_TO_PROMPT = "Enter a path in MEDITA_ROOT to save files (enter nothing for default): "
ENTER_BLANK_VALUE_PROMPT = "Set blank value to True? (y/N): "
ENTER_NULL_VALUE_PROMPT = "Set null value to True? (y/N): "
ENTER_UNIQUE_VALUE_PROMPT = "Set unique value to True? (y/N): "
ENTER_DEFAULT_NOW_DATE_PROMPT = "Wanna set default function to 'timezone.now'? (y/N): "
ENTER_DEFAULT_UUID_PROMPT = "Wanna set default uuid function to 'uuid.uuid4'? (y/N): "
ENTER_UUID_PRIMARY_KEY_PROMPT = "Wanna set this field to be primary key? (y/N): "
ENTER_TO_PROMPT = "What is the reference key for this field? ([app_name:]model_name): "
ENTER_FOREIGN_KEY_ON_DELETE_PROMPT = "Set the 'on delete' value for field [0-5]: "
ENTER_RELATED_NAME_PROMPT = "Enter a related name for your field (enter nothing for default): "
ENTER_UNICODE_ALLOWED_PROMPT = "Set unicode_allowed to True? (y/N): "

# main prompts
MAIN_PROMPT = "Enter a command: "
CREATE_MODEL_NAME_PROMPT = "Enter a name for model: "
ADD_FIELD_TYPE_PROMPT = "Enter a type [0-%d]: " % (len(DJANGO_FIELDS) + len(DJANGO_RELATION_FIELDS) - 1)
ADD_FIELD_NAME_PROMPT = "Enter a name for field: "
MODELS_PY_ALREADY_EXIST_PROMPT = "'models.py' already exists. Do you want to overwrite it? (y/N): "
FIELD_DELETE_CONFIRMATION_PROMPT = "Are you sure you want to delete this field? (y/N): "
MODEL_DELETE_CONFIRMATION_PROMPT = "Are you sure you want to delete this model? (y/N): "
RESET_ALL_MODELS_PROMPT = "Are you sure you want to reset everything?\nThis will delete all models. (y/N): "
RESET_ALL_FIELDS_PROMPT = "Are you sure you want to reset this model?\nThis will delete all fields of this model. (y/N): "
