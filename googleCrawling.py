from selenium import webdriver
import time
from urllib.parse import quote_plus
from selenium.webdriver.common.by import By
from urllib.request import urlopen
import os


driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?h1=ko&tab=ri&ogb1")

elem=driver.find_element(By.NAME,"q")
elem.send_keys("생두") #생두, 라이트 로스팅, 미디엄 로스팅, 다크 로스팅으로 바꿔가며 크롤링
elem.send_keys(Keys.RETURN)
SCROLL_PAUSE_TIME=1
last_height=driver.execute_script("return document.body.scrollHeight")
while True:
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight");)
  time.sleep(SCROLL_PAUSE_TIME)
  new_height=driver.execute_script("return document.body.scrollHeight")
  if new_height==last_height:
    try:
      driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
    except:
       break
    last_height=new_height

images=driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
count=1
for image in images:
  image.click()
  time.sleep(3)
  imgUrl=driver.find_element(By.CSS_SELECTOR,".n3VNCb").get_attribute("src")
  urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
  count=count+1