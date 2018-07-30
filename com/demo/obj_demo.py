"""
    类的创建和操作
"""


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        print('我是people的构造函数。。。')
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        print('我是student的构造函数。。。')
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


#多继承实例
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        print('我是speaker的构造函数')
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

    def __str__(self):
        return "我叫 %s，我是一个演说家，我演讲的主题是 %s，谢谢！"%(self.name,self.topic)

'''
    多重继承
    调用顺序：sample -> student -> people -> speaker
'''
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        print('我是sample的构造函数。。。。')
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

    #静态方法
    @staticmethod
    def doing(cls):
        print('%s doing some things!'%cls.a)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
test.doing(test)
print(test)

