
class Field_Builder:
    def __init__(self, name, field):
        self._name = name
        self._field = field

    def __repr__(self):
        return "\033[0;33m<field: <field_name: \033[1;33m%s\033[0;33m, field_type: \033[1;33m%s\033[0;33m>>\033[0;0m" % (self._name, self._field)

class Text_Choice_Builder:
    def __init__(self, name, val_list, repr_list):
        self._name = name
        self._choice_list = list(zip(val_list, repr_list))

    def get_name(self):
        return self._name

    def __str__(self):
        choices_str = "\t{} = [\n".format(self._name)
        for item in self._choice_list:
                choices_str += "\t\t('{}','{}'),\n".format(item[0], item[1])
        choices_str += "\t]\n"

        return choices_str

class Integer_Choice_Builder:
    def __init__(self, name, val_list, repr_list):
        self._name = name
        self._choice_list = list(zip(val_list, repr_list))

    def get_name(self):
        return self._name

    def __str__(self):
        choices_str = "\t{} = [\n".format(self._name)
        for item in self._choice_list:
                choices_str += "\t\t({},'{}'),\n".format(item[0], item[1])
        choices_str += "\t]\n"

        return choices_str

class BigIntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,choices=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.BigIntegerField"
        self._default = default
        self._choices = choices
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        choices = ""
        if self._choices:
            choices = "choices={},".format(self._choices.get_name())

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{choices}{blank}{null}{unique}".format(
                default=default, choices=choices, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class BooleanField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.BooleanField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default != None and self._default != '':
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class CharField_Builder(Field_Builder):

    def __init__(self,name,max_length,default=None,choices=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.CharField"
        self._max_length = max_length
        self._default = default
        self._choices = choices
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_length = "max_length={},".format(self._max_length)

        default = ""
        if self._default:
            default = "default='{}',".format(self._default)

        choices = ""
        if self._choices:
            choices = "choices={},".format(self._choices.get_name())

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{default}{choices}{blank}{null}{unique}".format(
                max_length=max_length, default=default, choices=choices, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class DateField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.DateField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class DateTimeField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.DateTimeField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class DecimalField_Builder(Field_Builder):

    def __init__(self,name,max_digits=None,decimal_places=None,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.DecimalField"
        self._max_digits = max_digits
        self._decimal_places = decimal_places
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_digits = ""
        if self._max_digits:
            max_digits = "max_digits={},".format(self._max_digits)

        decimal_places = ""
        if self._decimal_places:
            decimal_places = "decimal_places={},".format(self._decimal_places)

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_digits}{decimal_places}{default}{blank}{null}{unique}".format(
                max_digits=max_digits, decimal_places=decimal_places, default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class EmailField_Builder(Field_Builder):

    def __init__(self,name,max_length=254,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.EmailField"
        self._max_length = max_length
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_length = "max_length={},".format(self._max_length)

        default = ""
        if self._default:
            default = "default='{}',".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{default}{blank}{null}{unique}".format(
                max_length=max_length, default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class FileField_Builder(Field_Builder):

    def __init__(self,name,max_length=100,upload_to=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.FileField"
        self._max_length = max_length
        self._upload_to = upload_to
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_length = "max_length={},".format(self._max_length)

        upload_to = ""
        if self._upload_to:
            upload_to = "upload_to='{}',".format(self._upload_to)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{upload_to}{blank}{null}{unique}".format(
                max_length=max_length, upload_to=upload_to, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class FloatField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.FloatField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class ImageField_Builder(Field_Builder):

    def __init__(self,name,max_length=100,upload_to=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.ImageField"
        self._max_length = max_length
        self._upload_to = upload_to
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_length = "max_length={},".format(self._max_length)

        upload_to = ""
        if self._upload_to:
            upload_to = "upload_to='{}',".format(self._upload_to)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{upload_to}{blank}{null}{unique}".format(
                max_length=max_length, upload_to=upload_to, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class IntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,choices=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.IntegerField"
        self._default = default
        self._choices = choices
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        choices = ""
        if self._choices:
            choices = "choices={},".format(self._choices.get_name())

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{choices}{blank}{null}{unique}".format(
                default=default, choices=choices, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class PositiveBigIntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,choices=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.PositiveBigIntegerField"
        self._default = default
        self._choices = choices
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        choices = ""
        if self._choices:
            choices = "choices={},".format(self._choices.get_name())

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{choices}{blank}{null}{unique}".format(
                default=default, choices=choices, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class PositiveIntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.PositiveIntegerField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class PositiveSmallIntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.PositiveSmallIntegerField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class SlugField_Builder(Field_Builder):
    def __init__(self,name,unicode=False,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.SlugField"
        self._unicode = unicode
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default='{}',".format(self._default)

        unicode = ""
        if self._unicode:
            unicode = "allow_unicode={},".format(self._unicode)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{unicode}{default}{blank}{null}{unique}".format(
                unicode=unicode, default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class SmallIntegerField_Builder(Field_Builder):

    def __init__(self,name,default=None,choices=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.SmallIntegerField"
        self._default = default
        self._choices = choices
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        choices = ""
        if self._choices:
            choices = "choices={},".format(self._choices.get_name())

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{choices}{blank}{null}{unique}".format(
                default=default, choices=choices, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class TextField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.TextField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default='{}',".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class TimeField_Builder(Field_Builder):

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.TimeField"
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{default}{blank}{null}{unique}".format(
                default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class URLField_Builder(Field_Builder):

    def __init__(self,name,max_length=200,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.URLField"
        self._max_length = max_length
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        max_length = "max_length={},".format(self._max_length)

        default = ""
        if self._default:
            default = "default='{}',".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{default}{blank}{null}{unique}".format(
                max_length=max_length, default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class UUIDField_Builder(Field_Builder):

    def __init__(self,name,primary_key=False,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.UUIDField"
        self._primary_key = primary_key
        self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        primary_key = ""
        if self._primary_key:
            primary_key = "primary_key={},".format(self._primary_key)

        default = ""
        if self._default:
            default = "default={},".format(self._default)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{primary_key}{default}{blank}{null}{unique}".format(
                primary_key=primary_key, default=default, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class ManyToManyField_Builder(Field_Builder):

    def __init__(self,name,to,to_app,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ManyToManyField"
        self._to = to
        self._to_app = to_app
        self._related_name = related_name
        self._blank = blank
        self._null = null

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        to = self._to + ","

        related_name = ""
        if self._related_name:
            related_name = "related_name='{}',".format(self._related_name)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={}".format(self._null)

        param = "{to}{related_name}{blank}{null}".format(
                to=to, related_name=related_name, blank=blank, null=null)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class ForeignKeyField_Builder(Field_Builder):

    def __init__(self,name,to,to_app,on_delete,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ForeignKey"
        self._to = to
        self._to_app = to_app
        self._on_delete = on_delete
        self._related_name = related_name
        self._blank = blank
        self._null = null

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        to = self._to + ","

        on_delete = "on_delete={},".format(self._on_delete)

        related_name = ""
        if self._related_name:
            related_name = "related_name='{}',".format(self._related_name)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={}".format(self._null)

        param = "{to}{on_delete}{related_name}{blank}{null}".format(
                to=to, on_delete=on_delete, related_name=related_name, blank=blank, null=null)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class OneToOneField_Builder(Field_Builder):

    def __init__(self,name,to,to_app,on_delete,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.OneToOneField"
        self._to = to
        self._to_app = to_app
        self._on_delete = on_delete
        self._related_name = related_name
        self._blank = blank
        self._null = null

    def get_name(self):
        return self._name

    def get_field(self):
        return self._field

    def __str__(self):

        name = self._name

        field = self._field

        to = self._to + ","

        on_delete = "on_delete={},".format(self._on_delete)

        related_name = ""
        if self._related_name:
            related_name = "related_name='{}',".format(self._related_name)

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={}".format(self._null)

        param = "{to}{on_delete}{related_name}{blank}{null}".format(
                to=to, on_delete=on_delete, related_name=related_name, blank=blank, null=null)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class Model_Builder:

    def __init__(self,name,*fields):
        self.name = name
        self.fields = list(fields)

    def add_field(self,field):
        self.fields.append(field)

    def get_field(self, index):
        # index should be validated before it get passed to the function
        return self.fields[index]

    def remove_field(self,index):
        # index should be validated before it get passed to the function
        self.fields.remove(self.fields[index])

    def __repr__(self):
        return "\033[0;33m<model: <model_name: \033[1;33m%s\033[0;33m, model_fields_count: \033[1;33m%d\033[0;33m>>\033[0;0m" % (self.name, len(self.fields))

    def __str__(self):
        model_str = "class {model_name}(models.Model):\n".format(model_name=self.name)


        if self.fields:
            for field in self.fields:

                if hasattr(field,'_choices') and field._choices:
                    model_str += str(field._choices)
                model_str += "\t{field}\n".format(field=field)
        else:
            model_str += "\tpass\n"

        return model_str
