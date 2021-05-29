

DJANGO_FIELDS = [
    "BigIntegerField",
    "BooleanField",
    "CharField",
    "DateField",
    "DateTimeField",
    "DecimalField",
    "EmailField",
    "FileField",
    "FloatField",
    "ImageField",
    "IntegerField",
    "PositiveBigInteger",
    "PositiveInteger"
    "PositiveSmallInteger",
    "SlugField",
    "SmallIntegerField",
    "TextField",
    "TimeField",
    "URLField",
    "UUIDField",
]

DJANGO_RELATION_FIELDS = [
    "ForeignKey",
    "ManyToManyField",
    "OneToOneField",
]

DJANGO_ON_DELETE_ACTIONS = [
    "models.CASCADE",
    "models.RESTRICT",
    "models.PROTECT",
    "models.SET_NULL",
    "models.SET_DEFAULT",
    "models.DO_NOTHING",
]

class BigIntegerField_Builder:

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.BigIntegerField"
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

class BooleanField_Builder:

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

class CharField_Builder:

    def __init__(self,name,max_length,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.CharField"
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

class DateField_Builder:

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

class DateTimeField_Builder:

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

class DecimalField_Builder:

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

class EmailField_Builder:

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

class FileField_Builder:

    def __init__(self,name,max_length=100,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.FileField"
        self._max_length = max_length
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

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{blank}{null}{unique}".format(
                max_length=max_length, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class FloatField_Builder:

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

class ImageField_Builder:

    def __init__(self,name,max_length=100,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.ImageField"
        self._max_length = max_length
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

        blank = ""
        if self._blank:
            blank = "blank={},".format(self._blank)

        null = ""
        if self._null:
            null = "null={},".format(self._null)

        unique = ""
        if self._unique:
            unique = "unique={}".format(self._unique)

        param = "{max_length}{blank}{null}{unique}".format(
                max_length=max_length, blank=blank, null=null, unique=unique)

        if param and param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class IntegerField_Builder:

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.IntegerField"
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

class PositiveBigIntegerField_Builder:

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.PositiveBigIntegerField"
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

class PositiveIntegerField_Builder:

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

class PositiveSmallIntegerField_Builder:

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

class SmallIntegerField_Builder:

    def __init__(self,name,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.SmallIntegerField"
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

class TextField_Builder:

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

class TimeField_Builder:

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

class URLField_Builder:

    def __init__(self,name,max_length,default=None,blank=False,null=False,unique=False):
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

class UUIDField_Builder:

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

class ManyToManyField_Builder:

    def __init__(self,name,to,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ManyToManyField"
        self._to = to
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

class ForeignKeyField_Builder:

    def __init__(self,name,to,on_delete,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ForeignKey"
        self._to = to
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

class OneToOneField_Builder:

    def __init__(self,name,to,on_delete,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.OneToOneField"
        self._to = to
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
        self.fields = list()
        self.fields.extend(fields)

    def add_field(self,field):
        self.fields.append(field)

    def remove_field(self,index):
        # index should be validated befor it get passed to the function
        self.fields.remove(self.fields[index])

    def __str__(self):
        model_str = "class {model_name}(models.Model):\n".format(model_name=self.name)

        for field in self.fields:
            model_str += "\t{field}\n".format(field=field)

        return model_str