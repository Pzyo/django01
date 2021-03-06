from django.db import models

# Create your models here.

# 自定义字段

class MyCharField(models.Field):
    def __init__(self,max_length,*args,**kwargs):
        self.max_length = max_length
        # 调用父类的init方法
        super().__init__(max_length=max_length,*args,**kwargs)  # 一定是要关键字的形式传入

    def db_type(self, connection):
        """
        返回真正的数据类型及各种约束条件
        :param connection:
        :return:
        """
        return 'char(%s)'%self.max_length

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    register_time = models.DateField()  # 年月日
    # register_time = models.DateTimeField()  # 年月日 时分秒
    """
    DateField
    DateTimeField
        两个重要参数
        auto_now: 每次操作数据的时候 该字段会自动将当前时间更新
        auto_now_add: 在创建数据的时候会自动将当前创建时间记录下来  之后只要人为不修改就会一直不变
    """
    def __str__(self):
        return '对象: %s'%self.name

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    # 库存
    kucun = models.IntegerField(default=1000)
    # 卖出
    maichu = models.IntegerField(default=1000)

    # 一对多
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    # 多对多
    authors = models.ManyToManyField(to='Author')

    # 自定义字段使用
    myfield = MyCharField(max_length=16,null=True)

    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()  # varchar(254)  该字段类型不是给models看, 而是给校验型组件看的

    def __str__(self):
        return '对象:%s'%self.name

class Author(models.Model):
    name = models.CharField(max_length=32)
    age =models.IntegerField()
    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 电话号码用BigIntegerField或者CharField
    addr = models.CharField(max_length=64)