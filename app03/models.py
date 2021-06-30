from django.db import models

# Create your models here.

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
