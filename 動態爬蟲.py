from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#初始化瀏覽器
driver = webdriver.Chrome()
driver.implicitly_wait(10)#如果沒有設置網頁開啟等待時間，有可能在網頁還沒完全開啟就進行爬蟲
driver.get('https://www.google.com')

#find_element(): 用來取得網頁中的第一個定位到的HTML元素。
#find_elements(): (名稱中多了一個s)，用來取得所有網頁中定位到的元素

search = driver.find_element(By.NAME,'q')#定位搜尋框
search.send_keys('aaron')#往搜尋框輸入aaron
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2) #程式會停2秒
print(driver.page_source)
items = driver.find_elements(By.CLASS_NAME,'LC20lb')
print(items)
addrs = driver.find_elements(By.CLASS_NAME,'yuRUbf')
print(addrs)

for a in addrs:
    print(a.find_element(By.TAG_NAME,'a').get_attribute('href'))
all = zip(items,addrs)
for i,a in all:
    print(f'{i.text}:{a.find_element(By.TAG_NAME,'a').get_attribute('href')}')


    

