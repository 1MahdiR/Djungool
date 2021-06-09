#
# Clients for building fields
# By Ray (__mr__)
#
# The value that user enters won't get validated!
# such as empty strings, alnum(), etc.
#

from model_builder import *

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

def BigIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = BigIntegerField_Builder(name,default,blank,null,unique)

	return field

def BooleanField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = BooleanField_Builder(name,default,blank,null,unique)

	return field

def CharField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(32))
	if not max_length:
		max_length = 32

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = CharField_Builder(name,max_length,default,blank,null,unique)

	return field

def DateField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DateField_Builder(name,default,blank,null,unique)

	return field

def DateTimeField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DateTimeField_Builder(name,default,blank,null,unique)

	return field

def DecimalField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_digits = input(ENTER_MAX_DIGIT_PROMPT.format(10))
	if not max_digits:
		max_digits = 10

	decimal_places = input(ENTER_DECIMAL_PLACES_PROMPT.format(3))
	if not decimal_places:
		decimal_places = 3

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DecimalField_Builder(name,max_digits,decimal_places,default,blank,null,unique)

	return field

def EmailField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(254))
	if not max_length:
		max_length = 254

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = EmailField_Builder(name,max_length,default,blank,null,unique)

	return field

def FileField_client(name):

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(100))
	if not max_length:
		max_length = 100

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = FileField_Builder(name,max_length,blank,null,unique)

	return field

def FloatField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = FloatField_Builder(name,default,blank,null,unique)

	return field

def ImageField_client(name):

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(100))
	if not max_length:
		max_length = 100

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = ImageField_Builder(name,max_length,blank,null,unique)

	return field

def IntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = IntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveBigIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveBigIntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveIntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveSmallIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveSmallIntegerField_Builder(name,default,blank,null,unique)

	return field

def SmallIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = SmallIntegerField_Builder(name,default,blank,null,unique)

	return field

def TextField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = TextField_Builder(name,default,blank,null,unique)

	return field

def TimeField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = TimeField_Builder(name,default,blank,null,unique)

	return field

def URLField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(200))
	if not max_length:
		max_length = 200

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = URLField_Builder(name,max_length,default,blank,null,unique)

	return field

def UUIDField_client(name):

	default = input(ENTER_DEFAULT_UUID_PROMPT)
	if default.lower() == 'y':
		default = 'uuid.uuid4'
	else:
		default = ''

	primary_key = input(ENTER_UUID_PRIMARY_KEY_PROMPT)
	if primary_key.lowet() == 'y':
		primary_key = True
	else:
		primary_key = False

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = UUIDField_Builder(name,max_length,default,blank,null,unique)

	return field
