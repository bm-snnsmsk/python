from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.github.com/"
driver.get(url)

time.sleep(2)

driver.maximize_window()
driver.save_screenshot("github.png")
print("driver başlığı : ",driver.title)


newUrl = "https://github.com/bm-snnsmsk/"
driver.get(url)

time.sleep(2)
driver.back()
# driver.forward()
time.sleep(2)

driver.close()

