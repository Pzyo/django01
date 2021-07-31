from django.db import models
from django.contrib.auth.models import User, AbstractUser

# 第一种: 一对一关系 (不推荐)
# class UserDetail(models.Model):
#     phone = models.BigIntegerField()
#     user = models.OneToOneField(to='User')

# 第二种: 利用面向对象的继承
class UserInfo(AbstractUser):
    """
    如果继承了AbstractUser
    那么在执行数据库迁移命令的时候auth_user表就不会再创建出来了
    而UserInfo表中会出现auth_user所有的字段外加自己扩展的字段

    这么做的好处在于能够直接点击你自己的表, 更加快速完成操作及扩容

    前提:
        1. 在继承之前没有执行过数据库迁移命令
            auth_user没有被创建出来, 如果当前库已经创建那么你就重新换一个库
        2. 继承的类里面不要覆盖AbstractUser里面的字段名
            表里面有的字段都不要动, 只扩展额外字段即可
        3. 需要在配置文件中告诉django你要用UserInfo替代auth_user
            AUTH_USER_MODEL = 'app08.UserInfo'
                                '应用名.表名'
    """
    phone = models.BigIntegerField()