from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
"""
url = "https://www.google.com/"
#driver = webdriver.Chrome(executable_path="E:\\current\\selenium\\pythonProject\\chromedriver\\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="E:\\current\\selenium\\pythonProject\\chromedriver\\chromedriver.exe")

s = Service("E:\\current\\selenium\\pythonProject\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

try:
    driver.get(url=url)
    time.sleep(5)

    driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
"""