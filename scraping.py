from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# chromedriverのパスを指定
driver_path = "chromedriver.exe"
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Qiitaトップページにアクセス
url = "https://qiita.com/"
driver.get(url=url)

###############　ここからログインボタンをクリックする処理 ###############
# コピーしたCSSセレクタを文字列に格納
#time.sleep(10)

# css_selector = "#GlobalHeader-react-component-f189acf6-a4b3-41e1-83c6-4fa00025cafc > header > div > div:nth-child(2) > a.style-1sn73cs"
# login_button_element = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
# #login_button_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

css_selector = "#GlobalHeader-react-component-f189acf6-a4b3-41e1-83c6-4fa00025cafc > header > div > div:nth-child(2) > a.style-1sn73cs"
login_button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


# ログインボタンを構成するHTMLタグを出力
print(login_button_element.get_attribute(name="outerHTML"))

# ログインボタンをクリック
login_button_element.click()
# 別のクリック方法(JavaScriptにクリック処理をさせる。処理が安定しています。)
# driver.execute_script("arguments[0].click();", login_button_element)