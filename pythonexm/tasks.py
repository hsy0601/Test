#获取知识星球登录页

from urllib import request
import re

URL='http://wx.zsxq.com/dweb/#/login'
res=request.urlopen(URL)
html_page=res.read().decode('utf8')
print(html_page)

#获取微信登陆四个字
data=re.findall('<title>(.*)</title>',html_page)
print(data[0])

#将数据保存到test.txt文件
with open('test.txt','w',encoding='utf8') as out_file:
    out_file.write(data[0])
    out_file.close()
    
