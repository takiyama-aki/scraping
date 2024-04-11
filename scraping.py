from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriverのパスを指定
driver = webdriver.Chrome()

# Qiitaトップページにアクセス
url = "https://qiita.com/"
driver.get(url)

xpath = r'/html/body/div[1]/div[1]/header/div/div[2]/a[1]'
element = driver.find_element(By.XPATH, xpath)

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, xpath))
# )
element.click()
