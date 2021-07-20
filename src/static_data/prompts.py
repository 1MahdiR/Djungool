from model_builder_statics import DJANGO_FIELDS, DJANGO_RELATION_FIELDS

# field_menu prompts
ENTER_DEFAULT_VALUE_PROMPT = "Enter a default value (enter nothing for no default): "
ENTER_MAX_LENGTH_PROMPT = "Enter a value for max length ({}): "
ENTER_MAX_DIGIT_PROMPT = "Enter a value for max digit ({}): "
ENTER_DECIMAL_PLACES_PROMPT = "Enter a value for decimal places ({}): "
ENTER_BLANK_VALUE_PROMPT = "Set blank value to True? (y/N): "
ENTER_NULL_VALUE_PROMPT = "Set null value to True? (y/N): "
ENTER_UNIQUE_VALUE_PROMPT = "Set unique value to True? (y/N): "
ENTER_DEFAULT_NOW_DATE_PROMPT = "Wanna set default function to 'timezone.now'? (y/N): "
ENTER_DEFAULT_UUID_PROMPT = "Wanna set default uuid function to 'uuid.uuid4'? (y/N): "
ENTER_UUID_PRIMARY_KEY_PROMPT = "Wanna set this field to be primary key? (y/N): "
ENTER_TO_PROMPT = "What is the reference key for this field?: "
ENTER_FOREIGN_KEY_ON_DELETE_PROMPT = "Set the 'on delete' value for field [0-5]: "
ENTER_RELATED_NAME_PROMPT = "Enter a related name for your field: "
ENTER_UNICODE_ALLOWED_PROMPT = "Set unicode_allowed to True? (y/N): "

# main prompts
MAIN_PROMPT = "Enter a command: "
CREATE_MODEL_NAME_PROMPT = "Enter a name for model: "
ADD_FIELD_TYPE_PROMPT = "Enter a type [0-%d]: " % (len(DJANGO_FIELDS) + len(DJANGO_RELATION_FIELDS) - 1)
ADD_FIELD_NAME_PROMPT = "Enter a name for field: "