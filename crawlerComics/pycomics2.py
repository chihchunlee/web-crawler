from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

driver = Chrome(executable_path="/Users/lee-chih-chun/PycharmProjects/web-crawler/crawlerComics/chromedriver")

# 武煉巔峰
# url = "https://www.cocomanga.com/12202/"
# 元尊
# url = "https://www.cocomanga.com/10136/"
# 重生之都市修仙
# url = "https://www.cocomanga.com/12214/"
# 學士再生
# url = "https://www.cocomanga.com/12221/"
# 劍逆蒼穹
# url = "https://www.cocomanga.com/12297/"
# 滄元圖
# url = "https://www.cocomanga.com/16368/"
# 凡人修仙傳
# url = "https://www.cocomanga.com/16465/"
# 凡人修仙傳 仙界篇
# url = "https://www.cocomanga.com/17529/"

# 因為有hcaptch擋住 再找時間研究破解 暫時一次一項

driver.get(url)

# 列出title
print(driver.title)

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
        print(link.get('title'))
        print("https://www.cocomanga.com" + link.get('href'))

    if count > 5 :
        break

time.sleep(5)
print("=" * 30)

time.sleep(5)

# driver關閉
driver.quit()






