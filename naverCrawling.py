from selenium import webdriver
import time
from urllib.parse import quote_plus
from selenium.webdriver.common.by import By
from urllib.request import urlopen
import os

def save_images(images,save_path):
  for index,image in enumerate(images[:1000]):
    src=image.get_attribute('src')
    t=urlopen(src).read()
    file=open(os.path.join(save_path,str(index+1)+'.jpg'),"wb")
    file.write(t)
    print("img save"+save_path+str(index+1)+".jpg")

def create_folder_if_not_exists(directory):
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
    except OSError:
      print('Error: Creating directory.'+directory)

def make_url(search_term):
  base_url='https://search.naver.com/search.naver?where=image&section=image&query='

def crawl_images(search_term):
  url=make_url(search_term)

  browser=webdriver.Chrome('chromedriver')
  browser.implicitly_wait(30)
  browser.get(url)
  time.sleep(5)

  for_in range(10000):
    browser.execute_script("window.scrollBy(0,30000)")
  
  images=browser.find_elements(By.CLASS_NAME,"_image")

  save_path="C:\coffee"+search_term+"/"
  create_folder_if_not_exists(save_path)
  save_images(images,save_path)
  print(search_term+"저장 성공!")
  browser.close()

if__name__=='__main__':
  crawl_images(input('원하는 검색어:'))