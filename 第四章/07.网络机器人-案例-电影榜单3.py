import requests
import csv
from lxml import html

#常量
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

#保存电影数据， 保存为csv文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "宣传语", "简介"])
        writer.writeheader() #写入表头
        writer.writerows(all_movies) #写入数据


#获取电影详情
def get_movie_info(movie_info_url):
    # 1.发送请求,获取电影详细数据
    movie_response = requests.get(movie_info_url, timeout=60)
    print(f"发送请求{movie_info_url}，获取电影详细数据...")


    # 2. 解析数据，获取电影详情
    movie_doc = html.fromstring(movie_response.text)

    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()") #电影名称
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()") #上映年份
    movie_datas = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()") #上映时间
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text") #类型
    movie_cost_times = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()") # 时长
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent") # 评分
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()") #语言
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()") #导演
    movie_authors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[4]/p[1]/a/text()") #作者
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text") #宣传语
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()") # 简介

    # 3. 返回电影详情 - 字典
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": movie_years[0].strip() if movie_years else '',
        "上映时间": movie_datas[0].strip() if movie_datas else '',
        "类型": ",".join(movie_tags) if movie_tags else '',
        "时长": movie_cost_times[0].strip() if movie_cost_times else '',
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "作者": ",".join(movie_authors) if movie_authors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else '',
    }
    for k,v in movie_info.items():
        if v is None:
            movie_info[k] = ''
        elif isinstance(v, str):
            movie_info[k] = v.strip()
    print(movie_info)
    return movie_info


#主函数,定义核心逻辑
def main():
    #1.发送请求，获取电影高分榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=60)
    print("发送请求，获取TMDB电影榜单数据")

    #2.解析数据，获取电影列表
    document = html.fromstring(response.text)
    movie_list = document.xpath("//div[@class='media-list-results contents']/div")

    #3.遍历电影列表，获取电影详情
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            #电影详情的url
             movie_info_url = TMDB_BASE_URL + movie_urls[0]
            #发送请求，获取电影详情数据
             movie_info = get_movie_info(movie_info_url)
             all_movies.append(movie_info)

    #4.保存数据，写入csv文件
    print("获取所有的电影详情，保存电影数据到csv文件中...")
    save_all_movies(all_movies)



if __name__ == '__main__':
    main()