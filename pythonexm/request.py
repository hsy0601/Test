import urllib.request

#def saveFile(data):
  #  path="D:\\python例子\\file"
    #f=open(path,'wb')
    #f.write(data)
    #f.close()

url="https://www.douban.com"
headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,like Gecko)'
              'Chrome/51.0.2704.63 Safari/537.36'}
req=urllib.request.Request(url=url,headers=headers)
res=urllib.request.urlopen(req)
data=res.read()
#saveFile(data)
data=data.decode('utf-8')
print(data)

print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())
