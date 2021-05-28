

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

class CharField_Builder:

    def __init__(self,name,max_digits,default=None,blank=False,null=False,unique=False):
        self._name = name
        self._field = "models.CharField"
        self._max_digits = max_digits
        self._default = None
        if default:
            self._default = default
        self._blank = blank
        self._null = null
        self._unique = unique

    def __str__(self):

        name = self._name

        field = self._field

        max_digits = "max_digits={},".format(self._max_digits)

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

        param = "{max_digits}{default}{blank}{null}{unique}".format(
                max_digits=max_digits, default=default, blank=blank, null=null, unique=unique)
        
        if param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class ManyToMany_Field_Builder:

    def __init__(self,name,to,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ManyToManyField"
        self._to = to
        self._related_name = related_name
        self._blank = blank
        self._null = null
    
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
        
        if param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)
    
class ForeignKey_Field_Builder:

    def __init__(self,name,to,on_delete,related_name=None,blank=False,null=False):
        self._name = name
        self._field = "models.ForeignKey"
        self._to = to
        self._on_delete = on_delete
        self._related_name = related_name
        self._blank = blank
        self._null = null
    
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
        
        if param[-1] == ",":
            param = param[:-1]

        return "{name} = {field}({param})".format(
                name=name, field=field, param=param)

class Model_Builder:
    pass

