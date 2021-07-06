from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    # 性别
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    )
    gender = models.IntegerField(choices=gender_choices)

    score_choices = (
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '及格'),
        ('D', '不及格'),
    )
    # 保证字段类型跟列举出来的元组第一个数据类型一致即可
    # score = models.CharField(choices=score_choices,null=True)
    """
    该gender字段存的还是数字, 但是如果存的数字在上面的元组范围之内
    那么可以非常轻松的获取到数字对应的真正的内容
    
    1. gender字段存的数字不在上述元组列表的范围内容
    2. 如果在 如何获取对应的中文信息
    """

# class Book(models.Model):
#     name = models.CharField(max_length=32)
#     authors = models.ManyToManyField(to='Author',
#                                     through='Book2Author',
#                                     through_fields=('book','author'))

# class Author(models.Model):
#     name = models.CharField(max_length=32)
    # books = models.ManyToManyField(to='Book',
    #                                 through='Book2Author',
    #                                 through_fields=('author', 'book'))

"""
through_fields字段先后顺序
    判断的本质:
        通过第三张表查询对应的表  需要用到哪个字段就把哪个字段放前面
    简单理解
        当前表是谁 就把对应的关联按字段放前面
"""
# class Book2Author(models.Model):
#     book = models.ForeignKey(to='Book')
#     author = models.ForeignKey(to='Author')