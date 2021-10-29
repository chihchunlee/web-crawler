import requests
import time
from bs4 import BeautifulSoup
import json

url = "https://www.manhuagui.com/comic/"
useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

headers = {'User-Agent': useragent,
           'Referer': 'https://www.manhuagui.com'}

# 指定漫畫書
# 全職法師29821 星武神決20568 從前有座靈劍山17102 百鍊成神19785 黑色五葉草16460 咒術回戰28004 英雄學院13885
# 王者天下4841 一拳超人7580 鬥破穹蒼7620  轉生成史萊姆那些事17023 無職轉生14798 哥布林殺手20515 回復術士26332
# 神印王座7896 萬界仙蹤26492 御靈師21326 拳願奧米加30782

# 一次只能英文限1000字 中文限854字
# comics = ["19785", "29821", "17102", "21326"]
comics = ["26492", "20568", "7896", "16460", "28004", "13885", "30782", "4841",
          "7580", "17023", "14798", "20515", "26332"]

# 全部整理整一個str
article = ""

for comic in comics:
    res = requests.get(url+comic, headers=headers)
    # print(res.url)

    # 書名取得
    soup = BeautifulSoup(res.content, 'lxml')
    titles = soup.select_one("body > div.w998.bc.cf > div.fl.w728 > div.book-cont.cf > div.book-detail.pr.fr > div.book-title ")
    # print(titles.text)

    # 書名加入
    article = article + titles.text + "\n"

    # 內容取得
    tags = soup.select("#chapter-list-1 > ul > li > a ")

    # 條件篩選 標籤只要有new的
    # 無new的給個提示
    new = 0

    for tag in tags:
        if tag.em is not None:
            new += 1
            # print(tag.attrs)

            # 話數 url 加入
            article = article + tag.attrs['title'] + "\nhttps://www.manhuagui.com" + tag.attrs['href'] + "\n"
            # print(tag.attrs['title'])
            # print("https://www.manhuagui.com" + tag.attrs['href'])
            # print(new)

    # print("更新了"+str(new)+"話")
    upd = "更新了"+str(new)+"話"
    # 加入更新
    article = article + upd + "\n"+"\n"
    # print("="*30)
    time.sleep(5)

# print(article)
# print(type(article))
print(len(article))


with open("setting.json", "r", encoding="utf8" ) as jfile:
    jdata = json.load(jfile)


token = jdata["TOKEN"]

headers2 = {
    "Authorization" : "Bearer " + token,
    "Content-Type" : "application/x-www-from-urlencoded"
}

params = {"message": "\n"+article}


url = "https://notify-api.line.me/api/notify"

r = requests.post(url, headers=headers2, params=params)

if r.status_code == 200:
    print("已經送出通知訊息...")

else:
    print("錯誤!送出失敗")