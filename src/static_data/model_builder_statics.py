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
    "PositiveInteger",
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
