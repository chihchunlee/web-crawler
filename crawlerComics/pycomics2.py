from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

driver = Chrome(executable_path="/Users/lee-chih-chun/PycharmProjects/web-crawler/crawlerComics/chromedriver")


# url = "https://www.cocomanga.com/12202/"
url = "https://www.cocomanga.com/10136/"
# url = "https://www.cocomanga.com/12214/"
# url = "https://www.cocomanga.com/12221/"
# url = "https://www.cocomanga.com/12297/"
# url = "https://www.cocomanga.com/16368/"
# url = "https://www.cocomanga.com/16465/"
# url = "https://www.cocomanga.com/17529/"

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

    if count > 2 :
        break

time.sleep(5)
print("=" * 30)

time.sleep(10)

# driver關閉
driver.quit()




