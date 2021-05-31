import unittest
import sys
sys.path.append('..')

from src.model_builder import *

class TestFieldBuilderClasses(unittest.TestCase):

    def test_BigIntegerField_1(self):

        field = BigIntegerField_Builder(
        'Number',default=123,blank=True,null=False
        )

        self.assertEqual(field.get_field(),
        'models.BigIntegerField'
        )

        self.assertEqual(str(field),
        'Number = models.BigIntegerField(default=123,blank=True)'
        )

    def test_BigIntegerField_2(self):

        field = BigIntegerField_Builder(
        'big_integer',unique=True
        )

        self.assertEqual(field.get_field(),
        'models.BigIntegerField'
        )

        self.assertEqual(str(field),
        'big_integer = models.BigIntegerField(unique=True)'
        )

    def test_BooleanField_1(self):

        field = BooleanField_Builder(
        'my_bool', default=False, null=True
        )

        self.assertEqual(field.get_field(),
        'models.BooleanField'
        )

        self.assertEqual(str(field),
        'my_bool = models.BooleanField(default=False,null=True)'
        )

    def test_BooleanField_2(self):

        field = BooleanField_Builder(
        'another_boolean', null=False
        )

        self.assertEqual(field.get_field(),
        'models.BooleanField'
        )

        self.assertEqual(str(field),
        'another_boolean = models.BooleanField()'
        )

    def test_CharField_1(self):

        field = CharField_Builder(
        'thisIsAText',64,default=None,blank=True,null=True
        )

        self.assertEqual(field.get_field(),
        'models.CharField'
        )

        self.assertEqual(str(field),
        'thisIsAText = models.CharField(max_length=64,blank=True,null=True)'
        )

    def test_CharField_2(self):

        field = CharField_Builder(
        'Text',max_length=128,default="",blank=True,null=False
        )

        self.assertEqual(field.get_field(),
        'models.CharField'
        )

        self.assertEqual(str(field),
        'Text = models.CharField(max_length=128,blank=True)'
        )

    def test_DateField_1(self):

        field = DateField_Builder(
        'My_DATE',default="timezone.now",null=True
        )

        self.assertEqual(field.get_field(),
        'models.DateField'
        )

        self.assertEqual(str(field),
        'My_DATE = models.DateField(default=timezone.now,null=True)'
        )

    def test_DateField_2(self):

        field = DateField_Builder(
        'date',null=False
        )

        self.assertEqual(field.get_field(),
        'models.DateField'
        )

        self.assertEqual(str(field),
        'date = models.DateField()'
        )

    def test_DateTimeField_1(self):

        field = DateTimeField_Builder(
        'datetime'
        )

        self.assertEqual(field.get_field(),
        'models.DateTimeField'
        )

        self.assertEqual(str(field),
        'datetime = models.DateTimeField()'
        )

    def test_DateTimeField_2(self):

        field = DateTimeField_Builder(
        'mdtf',null=True
        )

        self.assertEqual(field.get_field(),
        'models.DateTimeField'
        )

        self.assertEqual(str(field),
        'mdtf = models.DateTimeField(null=True)'
        )

    def test_DecimalField_1(self):

        field = DecimalField_Builder(
        'my_number',max_digits=10,decimal_places=11,null=True
        )

        self.assertEqual(field.get_field(),
        'models.DecimalField'
        )

        self.assertEqual(str(field),
        'my_number = models.DecimalField(max_digits=10,decimal_places=11,null=True)'
        )

    def test_DecimalField_2(self):

        field = DecimalField_Builder(
        'a_Decimal',max_digits=None,decimal_places=3,unique=True,default=123.123
        )

        self.assertEqual(field.get_field(),
        'models.DecimalField'
        )

        self.assertEqual(str(field),
        'a_Decimal = models.DecimalField(decimal_places=3,default=123.123,unique=True)'
        )

    def test_EmailField_1(self):

        field = EmailField_Builder(
        'email',blank=True,max_length=256,unique=True
        )

        self.assertEqual(field.get_field(),
        'models.EmailField'
        )

        self.assertEqual(str(field),
        'email = models.EmailField(max_length=256,blank=True,unique=True)'
        )

    def test_EmailField_2(self):

        field = EmailField_Builder(
        'my_email',null=False,unique=True,default=""
        )

        self.assertEqual(field.get_field(),
        'models.EmailField'
        )

        self.assertEqual(str(field),
        'my_email = models.EmailField(max_length=254,unique=True)'
        )

    def test_FileField_1(self):

        field = FileField_Builder(
        'my_file',null=False,max_length=128
        )

        self.assertEqual(field.get_field(),
        'models.FileField'
        )

        self.assertEqual(str(field),
        'my_file = models.FileField(max_length=128)'
        )

    def test_FileField_2(self):

        field = FileField_Builder(
        'another_file',null=True
        )

        self.assertEqual(field.get_field(),
        'models.FileField'
        )

        self.assertEqual(str(field),
        'another_file = models.FileField(max_length=100,null=True)'
        )

    def test_FloatField_1(self):

        field = FloatField_Builder(
        'floaty',null=True,blank=True
        )

        self.assertEqual(field.get_field(),
        'models.FloatField'
        )

        self.assertEqual(str(field),
        'floaty = models.FloatField(blank=True,null=True)'
        )

    def test_FloatField_2(self):

        field = FloatField_Builder(
        'pi',null=False,blank=False,default=3.14
        )

        self.assertEqual(field.get_field(),
        'models.FloatField'
        )

        self.assertEqual(str(field),
        'pi = models.FloatField(default=3.14)'
        )

    def test_ImageField_1(self):

        field = ImageField_Builder(
        'image',null=True,max_length=128
        )

        self.assertEqual(field.get_field(),
        'models.ImageField'
        )

        self.assertEqual(str(field),
        'image = models.ImageField(max_length=128,null=True)'
        )

    def test_ImageField_2(self):

        field = ImageField_Builder(
        'img',null=False
        )

        self.assertEqual(field.get_field(),
        'models.ImageField'
        )

        self.assertEqual(str(field),
        'img = models.ImageField(max_length=100)'
        )

    def test_IntegerField_1(self):

        field = IntegerField_Builder(
        'integer', default=147,null=True,blank=False
        )

        self.assertEqual(field.get_field(),
        'models.IntegerField'
        )

        self.assertEqual(str(field),
        'integer = models.IntegerField(default=147,null=True)'
        )

    def test_IntegerField_2(self):

        field = IntegerField_Builder(
        'num',null=False,blank=False
        )

        self.assertEqual(field.get_field(),
        'models.IntegerField'
        )

        self.assertEqual(str(field),
        'num = models.IntegerField()'
        )

    def test_PositiveBigIntegerField_1(self):

        field = PositiveBigIntegerField_Builder(
        'pos_int',default=123456,null=True
        )

        self.assertEqual(field.get_field(),
        'models.PositiveBigIntegerField'
        )

        self.assertEqual(str(field),
        'pos_int = models.PositiveBigIntegerField(default=123456,null=True)'
        )

    def test_PositiveBigIntegerField_2(self):

        field = PositiveBigIntegerField_Builder(
        'positive'
        )

        self.assertEqual(field.get_field(),
        'models.PositiveBigIntegerField'
        )

        self.assertEqual(str(field),
        'positive = models.PositiveBigIntegerField()'
        )

    def test_PositiveInteger_1(self):

        field = PositiveIntegerField_Builder(
        'pos_int',default=123,null=True,unique=True
        )

        self.assertEqual(field.get_field(),
        'models.PositiveIntegerField'
        )

        self.assertEqual(str(field),
        'pos_int = models.PositiveIntegerField(default=123,null=True,unique=True)'
        )

    def test_PositiveInteger_2(self):

        field = PositiveIntegerField_Builder(
        'another_positive',blank=False
        )

        self.assertEqual(field.get_field(),
        'models.PositiveIntegerField'
        )

        self.assertEqual(str(field),
        'another_positive = models.PositiveIntegerField()'
        )

    def test_PositiveSmallInteger_1(self):

        field = PositiveSmallIntegerField_Builder(
        'sml_int',default=10,unique=True
        )

        self.assertEqual(field.get_field(),
        'models.PositiveSmallIntegerField'
        )

        self.assertEqual(str(field),
        'sml_int = models.PositiveSmallIntegerField(default=10,unique=True)'
        )

    def test_PositiveSmallInteger_2(self):

        field = PositiveSmallIntegerField_Builder(
        'sml',unique=True,null=False
        )

        self.assertEqual(field.get_field(),
        'models.PositiveSmallIntegerField'
        )

        self.assertEqual(str(field),
        'sml = models.PositiveSmallIntegerField(unique=True)'
        )

    def test_SmallIntegerField_1(self):

        field = SmallIntegerField_Builder(
        'sml_int',null=True,blank=False
        )

        self.assertEqual(field.get_field(),
        'models.SmallIntegerField'
        )

        self.assertEqual(str(field),
        'sml_int = models.SmallIntegerField(null=True)'
        )

    def test_SmallIntegerField_2(self):

        field = SmallIntegerField_Builder(
        'number',blank=False,null=False,unique=False
        )

        self.assertEqual(field.get_field(),
        'models.SmallIntegerField'
        )

        self.assertEqual(str(field),
        'number = models.SmallIntegerField()'
        )

    def test_TextField_1(self):

        field = TextField_Builder(
        'my_text',blank=True,default="hello world",null=False
        )

        self.assertEqual(field.get_field(),
        'models.TextField'
        )

        self.assertEqual(str(field),
        'my_text = models.TextField(default=\'hello world\',blank=True)'
        )

    def test_TextField_2(self):

        field = TextField_Builder(
        'user_text',default=None,blank=False
        )

        self.assertEqual(field.get_field(),
        'models.TextField'
        )

        self.assertEqual(str(field),
        'user_text = models.TextField()'
        )

    def test_TimeField_1(self):

        field = TimeField_Builder(
        'time_user',default="timezone.now",null=True
        )

        self.assertEqual(field.get_field(),
        'models.TimeField'
        )

        self.assertEqual(str(field),
        'time_user = models.TimeField(default=timezone.now,null=True)'
        )

    def test_TimeField_2(self):

        field = TimeField_Builder(
        'time_wasted',null=False
        )

        self.assertEqual(field.get_field(),
        'models.TimeField'
        )

        self.assertEqual(str(field),
        'time_wasted = models.TimeField()'
        )

    def test_URLField_1(self):

        field = URLField_Builder(
        'urly',256,default=None,blank=True
        )

        self.assertEqual(field.get_field(),
        'models.URLField'
        )

        self.assertEqual(str(field),
        'urly = models.URLField(max_length=256,blank=True)'
        )

    def test_URLField_2(self):

        field = URLField_Builder(
        'link',200,default="https://google.com",blank=False,null=False
        )

        self.assertEqual(field.get_field(),
        'models.URLField'
        )

        self.assertEqual(str(field),
        'link = models.URLField(max_length=200,default=\'https://google.com\')'
        )

    def test_UUIDField_1(self):

        field = UUIDField_Builder(
        'user_key',primary_key=True,default="uuid.uuid4",null=False,unique=True
        )

        self.assertEqual(field.get_field(),
        'models.UUIDField'
        )

        self.assertEqual(str(field),
        'user_key = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)'
        )

    def test_UUIDField_2(self):

        field = UUIDField_Builder(
        'my_uuid',primary_key=False,null=True,blank=True
        )

        self.assertEqual(field.get_field(),
        'models.UUIDField'
        )

        self.assertEqual(str(field),
        'my_uuid = models.UUIDField(blank=True,null=True)'
        )

    def test_ManyToManyField_1(self):

        field = ManyToManyField_Builder(
        'humans','Human',related_name="books_human",null=False
        )

        self.assertEqual(field.get_field(),
        'models.ManyToManyField'
        )

        self.assertEqual(str(field),
        'humans = models.ManyToManyField(Human,related_name=\'books_human\')'
        )

    def test_ManyToManyField_2(self):

        field = ManyToManyField_Builder(
        'books','Book',related_name="humans_book",null=True
        )

        self.assertEqual(field.get_field(),
        'models.ManyToManyField'
        )

        self.assertEqual(str(field),
        'books = models.ManyToManyField(Book,related_name=\'humans_book\',null=True)'
        )

    def test_ForeignKey_1(self):

        field = ForeignKeyField_Builder(
        'teacher','Teacher','models.CASCADE',related_name="student_teacher",null=False
        )

        self.assertEqual(field.get_field(),
        'models.ForeignKey'
        )

        self.assertEqual(str(field),
        'teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name=\'student_teacher\')'
        )

    def test_ForeignKey_2(self):

        field = ForeignKeyField_Builder(
        'book','Book','models.DO_NOTHING',related_name="human_book",null=True
        )

        self.assertEqual(field.get_field(),
        'models.ForeignKey'
        )

        self.assertEqual(str(field),
        'book = models.ForeignKey(Book,on_delete=models.DO_NOTHING,related_name=\'human_book\',null=True)'
        )

    def test_OneToOneField_1(self):

        field = OneToOneField_Builder(
        'teamate','Student','models.DO_NOTHING',related_name="teamate",null=True
        )

        self.assertEqual(field.get_field(),
        'models.OneToOneField'
        )

        self.assertEqual(str(field),
        'teamate = models.OneToOneField(Student,on_delete=models.DO_NOTHING,related_name=\'teamate\',null=True)'
        )

    def test_OneToOneField_2(self):

        field = OneToOneField_Builder(
        'group','Group','models.CASCADE',related_name="group",null=False,blank=False
        )

        self.assertEqual(field.get_field(),
        'models.OneToOneField'
        )

        self.assertEqual(str(field),
        'group = models.OneToOneField(Group,on_delete=models.CASCADE,related_name=\'group\')'
        )





        




if __name__ == "__main__":
    unittest.main()
