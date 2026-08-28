import re

s1 = "18806065060是我的手机号，记住了吗？我的另一个手机号是18215149586，两个qq号分别是16854811 和 18658484891698 你记住了吗？"
s2 = "我的手机号是18806065060，记住了吗？我的另一个手机号是18215149586，两个qq号分别是16854811 和 18658484891698 你记住了吗？"

# match -从字符串的开头开始匹配（匹配第一个匹配项） --->match对象
result = re.match(r"1[3-9]\d{9}" , s1)
print(result.group()) #获取匹配的结果
print(result.span()) #获取匹配的索引
print(result.start()) #获取匹配的开始索引
print(result.end())

# reasear - 从任意位置开始，搜索第一个匹配项 ---> match对象
result = re.search(r"1[3-9]\d{9}" , s2)
print(result.group()) #获取匹配的结果
print(result.span()) #获取匹配的索引
print(result.start()) #获取匹配的开始索引
print(result.end())



# findall - 从任意位置开始，搜索所有匹配项 ---> list
result = re.findall(r"1[3-9]\d{9}" , s2)
print(result)



