# 导入正则表达式库
import re
search_code="afjaklxxIxxkkafakmlxxlovexxsdxxyouxxaq"
#.的使用,可以理解为一个占位符
# a='x123'
# b=re.findall("x.",a)
# print(b)

#*的使用,可以理解为匹配前一个字符0次或无限次
# a='xyxy123'
# b=re.findall("x*",a)
# print(b)

#?的使用,可以理解为匹配前一个字符0次或1次
# a='xy1x23'
# b=re.findall("x?",a)
# print(b)

#.*的使用 贪心算法 提取最多的内容
# b=re.findall("xx.*xx",search_code)
# print(b)

# #.*?的使用 非贪心算法 像一个婴儿,少量多餐
# c=re.findall("xx.*?xx",search_code)
# print(c)

#(.*?)的使用 提取括号中的内容
# d=re.findall("xx(.*?)xx",search_code)
# print(d)

# s='''kskxxI
# xxjdsjxxlovexxjjxxyouxxsdfj
# '''
# f=re.findall("xx(.*?)xx",s,re.S)
# print(f)

# 对比search和findall的区别
# s='jhahxxixx123xxlovexxhfbahxxyouxxaad'
# f=re.search

# 匹配数字
s='da223fskf34'
f=re.findall("(\d+)",s)
print(f)


