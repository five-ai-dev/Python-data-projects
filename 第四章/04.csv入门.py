#csv操作--方式一 : 文件操作的原始方式
#写
with open("csv_data/01.csv", "w", encoding = "utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n")  #写入表头
    f.write("小智,18,男,python\n") #写入数据
    f.write("小张,17,男,'insect,game'\n")
    f.write("小霞,16,女,java\n")
    f.write("小兰,17,女,read\n")

#读


#csv操作--方式二 : csv(推荐)
import csv

#写
with open("csv_data/02.csv", "w", encoding = "utf-8", newline = "") as f:
    writer = csv.DictWriter(f, fieldnames = ["姓名", "年龄", "性别", "爱好"])
    writer.writeheader()
    writer.writerow({"姓名": "小智", "年龄": 18, "性别": "男", "爱好": "python"})
    writer.writerow({"姓名": "小张", "年龄": 17, "性别": "男", "爱好": "insect, game"})
    writer.writerow({"姓名": "小霞", "年龄": 16, "性别": "女", "爱好": "java"})
    writer.writerow({"姓名": "小兰", "年龄": 17, "性别": "女", "爱好": "read"})

#读
with open("csv_data/02.csv", "r", encoding = "utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

