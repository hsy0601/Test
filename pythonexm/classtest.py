class JustCounter:
    __serectCount=0   #私有变量
    publicCount=0        #公开变量
    def count(self):
        self.__serectCount+=1
        self.publicCount+=1
        print(self.__serectCount)

counter=JustCounter()  #实例化类
counter.count()           #调用count函数
counter.count()
print(counter.publicCount)#外部无法访问私有变量


class Site:
    def __init__(self,name,url):
        self.name=name
        self.__url=url
    def who(self):
        print(self.name)
    def __foo(self):
        print('私有')
    def foo(self):
        print('公有')
        self.__foo()

s=Site('曾经存在的','www.eaer.com')
s.who()
