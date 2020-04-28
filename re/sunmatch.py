import re
import requests
f=open('source','r',encoding='utf-8')
html=f.read()
f.close()

pic_url=re.findall('img src="(.*?)" class="lessonimg"',html,re.S)
j=0
for i in pic_url:
    print(i)
    pic=requests.get(i)
    fp=open('pic\\'+str(j)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    j +=1
