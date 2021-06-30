from django.db import models

# Create your models here.


# 创建表关系  先将基表创建出来  然后再添加外键字段
class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')
    # 总共8位, 小数点后面占2位
    """
    图书和出版社是一对多 并且书是多的一方 所以外键字段放在书表里面
    """
    publish = models.ForeignKey(to='Publish')  # 默认就是与出版社表的外键字段做关联 to_field='id'
    """
    如果字段对应的是ForeignKey 那么orm会在publish字段后面加 _id
    如果你自作聪明加了_id那么orm还是会在后面自动加_id, 变成publish_id_id
    
    后面在定义ForeignKey的时候就不要自己加_id
    """

    """
    图书和作者是多对多的关系 外键字段建在任意一方均可 但是推荐建在查询频率较高的一方
    """
    authors = models.ManyToManyField(to='Author')

    """
    authors是一个虚拟字段 主要是用来告诉orm 书籍表和作者表是多对多的关系
    让orm自动帮你创建第三张关系表
    """

class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名')
    addr = models.CharField(max_length=32,verbose_name='出版社地址')

class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者名')
    age = models.IntegerField(verbose_name='年龄')
    """
    作者与作者详情是一对一的关系 外键字段建在任意一方即可 但推荐建在查询频率较高的表
    """
    author_detail = models.OneToOneField(to='AuthorDetail')
    """
    OneToOneField也会自动给字段加_id后缀
    所以也不用自己加_id
    """

class AuthorDetail(models.Model):
    phone = models.BigIntegerField(verbose_name='手机号')  # 或者直接用字符类型
    addr = models.CharField(max_length=32,verbose_name='地址')