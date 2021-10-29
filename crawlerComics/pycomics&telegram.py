from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import telegram
import json

driver = Chrome(executable_path="/Users/lee-chih-chun/PycharmProjects/web-crawler/crawlerComics/chromedriver")

url = "https://www.cocomanga.com/12202/"

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

token = jdata["TelegramBotToken"]
chat_id = jdata["chat_id"]

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return  bot.sendMessage(chat_id=chat_id, text=msg)

article = ""

driver.get(url)

# 列出title
# print(driver.title)
article = article + driver.title + "\n"

# 取得 page_source
html = driver.page_source

# 開始篩選資料
soup = BeautifulSoup(html,'lxml')
links = soup.select("a")

# count 只取3個
count = 0
for link in links:
    # 去掉 None
    if link.get('title') is not None:
        count += 1
        # print(link.get('title'))
        article = article + link.get('title') + "\n"
        # print("https://www.cocomanga.com" + link.get('href'))
        article = article + "https://www.cocomanga.com" + link.get('href') + "\n"

    if count > 5 :
        break

time.sleep(5)
print("=" * 30)

time.sleep(5)

# driver關閉
driver.quit()

# 發文
test = telegram_bot_sendText(article)

# print(article)
# print(len(article))

