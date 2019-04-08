class people:
    name=' '
    age=0        #基本属性
    __weight=0 #私有属性
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("'{}' 说: 我 '{}' 岁.".format(self.name,self.age))

class student(people):
    grade=' '
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)   #调用父类构造函数
        self.grade=g
    def speak(self):
        print("'{}' 说: 我 '{}' 岁.读'{}'年级".format(self.name,self.age,self.grade))

#s=student('ruirui',19,180,9)   #父类people无grade属性，此处不能调用
#s.speak()

class speaker():
    topic=' '
    name=' '
    def __init__(self,t,n):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫 '{}'，我是一个演说家，我演讲的主题是 '{}'".format(self.name,self.topic))

class sample(speaker,student):
    a=' '
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,t,n)

test=sample("Tim",25,80,4,"python")
test.speak()   #方法同名时，默认调用第一个继承的父类的方法

