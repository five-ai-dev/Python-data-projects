import re

s1 = "18806060011是我的手机号,188开头的,以00结尾的;我的另一个手机号是16600009999,两个qq号分别是1854652377和1542687455,邮箱为python666@163.com"

#正则表达式
# print(re.findall(r"188.*", s1)) # *匹配任何个
# print(re.findall(r"188.?", s1)) # ?匹配零个或一个(最多出现一次）
# print(re.findall(r"188.+", s1)) # +匹配一个或多个（最少出现一次）
#
# print(re.findall(r"188\d{8}", s1)) # \d{8}匹配8个数字
# print(re.findall(r"154\d{6,}", s1)) # \d{8,}匹配8个或多个数字
# print(re.findall(r"188\d{8,10}", s1)) # \d{8,10}匹配8到10个数字

# print(re.findall(r"1[38]\d{8}", s1)) # [38] 匹配3或者8
# print(re.findall(r"1[^38]\d{8}", s1)) # [^38] 匹配除3或者8
# print(re.findall(r"1[3-9]\d{8}", s1)) # [3-9] 匹配3到9(范围)
# print(re.findall(r"^1[38]\d{9}", s1)) # ^匹配字符串的开头
# print(re.findall(r"1[38]\d{9}$", s1)) # $匹配字符串的结尾

# print(re.findall(r"\w+@\w+\.\w+", s1)) #\w匹配任意字母数字下划线其他语言字符
# print(re.findall(r"\w+@\w+\.\w+", s1, re.ASCII))

#注意
s2 = "现在的时间是2026-08-20 14:55:05, 今天的天气还可以,气温28度"
print(re.findall(r"\d{4}-\d{2}-\d{2}", s2))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s2))






