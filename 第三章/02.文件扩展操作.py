#读文件
"""
路径写法：
       相对路径：从当前文件所在目录开始查找
           . 表示当前目录 --> ./resources/虞美人（李煜）.txt ./可以省略
           .. 表示上一级目录 --> ../resources/虞美人（李煜）.txt  #如果路径在第三章，想要去其他章则需要../去返回上一级目录




       绝对路径：从文件系统根目录开始查找,文件位置的完整路径（注意：反斜杠是转义字符，需要写成双反斜杠或者用斜杠代替）



"""

with open("./resources/虞美人（李煜）.txt", "r", encoding = "utf-8") as f:
#读取文件内容
    content = f.read()
    print(content)

#写文件内容
#a: append , 追加内容；w: write , 覆盖内容 -->文件不存在则创建文件
with open("resources/静夜思.txt", "a", encoding = "utf-8") as f:
     f.write("静夜思(李白)\n\n")
     f.write("床前明月光\n")
     f.write("疑似地上霜\n")
     f.write("举头望明月\n")
     f.write("低头思故乡\n")
