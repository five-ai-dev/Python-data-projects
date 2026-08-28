from lxml import html


# 读取html文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8")as f:
    html_text = f.read()


    #解析html的文本，将其转化为一个文档对象
    document = html.fromstring(html_text)

    # 解析表头 - xpath语法
    #/table/thead/tr/th/text()： 表示从根节点开始匹配
    #//table/thead/tr/th/text()： 表示从任意位置开始匹配
    # th_list = document.xpath("/html/body/div/div/table/thead/tr/th/text()")
    # th_list = document.xpath("//table/thead/tr/th/text()")
    th_list = document.xpath("//thead/tr/th/text()")
    print(th_list)

    # 第一行数据 - xpath语法
    td_list = document.xpath("//tbody/tr[1]/td/text()")
    print(td_list)

    # 最后一行数据 - xpath语法
    td_list = document.xpath("//tbody/tr[last()]/td/text()")
    print(td_list)

    # 倒数第二行数据 - xpath语法
    td_list = document.xpath("//tbody/tr[last() - 1]/td/text()")
    print(td_list)

    # p[@class]: 表示匹配所有class属性的p标签
    p_list = document.xpath("//p[@class]/text()")
    print(p_list)

    #p[@class='xn']： 表示匹配所有class属性为xn的p标签
    p_list = document.xpath("//p[@class='xn']/text()")
    print(p_list)

    # *： 表示匹配任意标签
    th_list = document.xpath("//thead/tr/*/text()")
    print(th_list)
    # @src： 表示匹配src属性
    # @*： 表示匹配任意属性
    # ti_list = document.xpath("//td/img/@src")
    ti_list = document.xpath("//td/img/@*")
    print(ti_list)






