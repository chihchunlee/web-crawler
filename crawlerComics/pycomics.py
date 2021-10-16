import requests
import time
from bs4 import BeautifulSoup

url = "https://www.manhuagui.com/comic/"
useragent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'

headers = {'User-Agent':useragent,
           'Referer':'https://www.manhuagui.com'}

# 指定漫畫書
# 黑色五葉草 咒術回戰 英雄學院 王者天下 一拳超人 鬥破穹蒼  史萊姆 無職轉生 回復術士
comics = ["16460","28004","13885","4841","7580","7620","17023","14798","26332"]

for comic in comics:
    res = requests.get(url+comic,headers=headers)
    # print(res.url)

    # 書名取得
    soup = BeautifulSoup(res.content,'lxml')
    title = soup.select_one("body > div.w998.bc.cf > div.fl.w728 > div.book-cont.cf > div.book-detail.pr.fr > div.book-title ")
    print(title.text)

    # 先測試是否一個可取得
    # tags = soup.select_one("#chapter-list-1 > ul > li > a ")
    # print(tags)
    # print(tags.text)
    # print(tags.get("href", None))
    # print(tags.span)

    # 再取全部
    tags = soup.select("#chapter-list-1 > ul > li > a ")

    # 條件篩選 標籤只要有new的
    # 無new的給個提示
    new = 0
    for tag in tags:

        if tag.em is not None:
            new += 1
            # print(tag.attrs)
            print(tag.attrs['title'])
            print("https://www.manhuagui.com" + tag.attrs['href'])
            # print(new)

    print("更新了"+str(new)+"話")
    print("="*30)

    time.sleep(2)