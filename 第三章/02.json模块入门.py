import json

#写入json数据文件
user = {
    "name":"小智",
    "age": 21,
    "gender": "男",
    "hobby": ["running, reading"]
}
with open("resources/user.json", "w", encoding = "utf-8") as f:
    #ensure_ascii: 默认为True，确保输出的所有数据都为ascii码（字母，数据，符号）如果为False，则输出中文不会乱码
    #indent: 会在输出的json数据中添加缩进
    json.dump(user, f, ensure_ascii=  False, indent = 4)

#读取json数据文件
with open("resources/user.json", "r", encoding = "utf-8") as f:
    user = json.load(f)
    print(user)
    print(type( user))