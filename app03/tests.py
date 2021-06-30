from django.test import TestCase

# Create your tests here.
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    import django
    django.setup()
    # 所有的代码都必须等待环境准备完毕之后才能书写
    from app03 import models

    # 增
    # res = models.User.objects.create(name='pzyo',age=18,register_time='2021-06-30')
    # print(res)
    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='tom',age=18,register_time=ctime)
    # user_obj.save()

    # 删
    res = models.User.objects.filter(pk=2).delete()
    print(res)
    """
    pk会自动查找当前表的主键字段 指代的就是当前表的主键字段
    用了pk之后, 就不需要知道当前表的主键字段到底叫什么
    """

