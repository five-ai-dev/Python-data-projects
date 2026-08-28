# #打开文件
# f = open("./resources/虞美人（李煜）.txt", "r", encoding = "utf-8")
# # #读取文件内容
# content = f.read()
# print(content)
#
# # content_list = f.readlines()
# # for line in content_list:
# #     print(line.strip())
#
# #关闭文件
# f.close()




#打开文件
#
# f = open("resources/静夜思.txt", "w", encoding = "utf-8")
#
# #添加文件内容
#
# f.write("静夜思(李白)\n\n")
# f.write("床前明月光\n")
# f.write("疑似地上霜\n")
# f.write("举头望明月\n")
# f.write("低头思故乡\n")
#
# print(content)
#
# #关闭文件
#
# f.close()



# -----------------------释放资源（方式一）---------------------------
#打开文件

f = open("resources/静夜思.txt", "w", encoding = "utf-8")
try:
#添加文件内容

     f.write("静夜思(李白)\n\n")
     f.write("床前明月光\n")
     f.write("疑似地上霜\n")
     f.write("举头望明月\n")
     f.write("低头思故乡\n")

     print(content)
finally:
   #关闭文件

   f.close()


# -----------------------释放资源（最佳方式）---------------------------
#打开文件

with open("resources/静夜思.txt", "w", encoding = "utf-8") as f:

     #添加文件内容
     f.write("静夜思(李白)\n\n")
     f.write("床前明月光\n")
     f.write("疑似地上霜\n")
     f.write("举头望明月\n")
     f.write("低头思故乡\n")

     print(content)
