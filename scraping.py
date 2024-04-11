from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# chromedriverのパスを指定
driver = webdriver.Chrome()

# 四季報オンライン
url = "https://shikiho.toyokeizai.net/"
driver.get(url)

login = r'/html/body/div[2]/div/div/header/div/div[3]/div[3]/button'
element1 = driver.find_element(By.XPATH, login)
element1.click()
time.sleep(5)

login2 = r'/html/body/div[2]/div/div/header/div/div[3]/div[3]/div/button'
element2 = driver.find_element(By.XPATH, login2)
element2.click()
time.sleep(5)

mail = r'/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[4]/input'
gmail = "hoge@mail.com"
mail = driver.find_element(By.NAME, "email")
mail.send_keys(gmail)
time.sleep(5)

password = r'/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[5]/input'
my_password = "MyPassword1"
element4 = driver.find_element(By.XPATH, password)
element4.send_keys(my_password)
time.sleep(5)

login3 = r'/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[7]/button'
element5 = driver.find_element(By.XPATH, login3)
element5.click()
time.sleep(5)