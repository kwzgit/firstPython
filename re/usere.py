# 导入re库文件
import re
f=open('test','r',encoding="utf-8")
html=f.read()
print(html)
f.close()

# 爬取链接
# links=re.findall('href="(.*?)"',html,re.S)
# for each in links:
#     print(each)
# 先抓大,再抓小
textFild=re.findall('<ul>(.*?)</ul>',html,re.S)[0]
short=re.findall('">(.*?)</a>',textFild,re.S)
print(short)