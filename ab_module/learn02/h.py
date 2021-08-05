
# 多继承的正确打开方式: mixins机制
# mixins机制核心: 就是在多继承背景下尽可能地提高多继承的可读性
# PS: 让多继承满足人的思维习惯 => 什么 "是" 什么

# 其实mixins机制就是一种命名规范, 以命名规范去解决多继承中父类间的关系

class Vehicle:  # 交通工具, 物品, 具有共同的属性和方法
    pass

# mixin类一般以Mixin、able、ible、MixIn结尾
class FlyMixin:  # 飞行器功能, 一般mixin是以功能为主, 而非一个物品
    def fly(self):
        pass

class CivilAircraft(FlyMixin, Vehicle): # 民航飞机
    pass

class Helicopter(FlyMixin, Vehicle): # 直升飞机
    pass

class Car(Vehicle): # 汽车
    pass

"""
1. 首先它必须表示某一种功能, 而不是某个物品, python 对于mixin类的命名方式一般以 Mixin, able, ible 为后缀
2. 其次它必须责任单一, 如果有多个功能, 那就写多个Mixin类, 一个类可以继承多个Mixin, 为了保证遵循继承的"is-a"原则, 只能继承一个标识其归属含义的父类
3. 然后, 它不依赖于子类的实现, 简单说就是该类能用于其他子类, 而非为某个子类定制
4. 最后, 子类即便没有继承这个Mixin类, 也照样可以工作, 就是缺少了某个功能。(比如飞机照样可以载客, 就是不能飞了)
"""
