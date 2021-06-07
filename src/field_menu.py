#
# Clients for building fields
# By Ray (__mr__)
#
# The value that user enters won't get validated!
# such as empty strings, alnum(), etc. 
#

from model_builder import *

ENTER_DEFAULT_VALUE_PROMPT = "Enter a default value (enter nothing for no default): "
ENTER_BLANK_VALUE_PROMPT = "Set blank value to True? (y/N): "
ENTER_NULL_VALUE_PROMPT = "Set null value to True? (y/N): "
ENTER_UNIQUE_VALUE_PROMPT = "Set unique value to True? (y/N): "

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