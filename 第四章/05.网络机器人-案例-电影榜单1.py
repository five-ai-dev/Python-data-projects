import requests
import csv
from lxml import html

#常量
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

#保存电影数据， 保存为csv文件
def save_all_movies(all_movies):
    pass


#获取电影详情
def get_movie_info(movie_info_url):
    pass


#主函数,定义核心逻辑
def main():
    #1.发送请求，获取电影高分榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=60)

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

    save_all_movies(all_movies)



if __name__ == '__main__':
    main()