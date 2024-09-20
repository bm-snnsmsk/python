from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

url = "https://www.github.com/"
driver.get(url)

arama_input = driver.find_element(By.NAME, "query-builder-test")
# arama_input = driver.find_element(By.NAME, "user_email")
time.sleep(1)
arama_input.send_keys("python")
time.sleep(2)
arama_input.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.page_source
print(result)

# result = driver.find_elements_by_css_selector(".repo-list-item h3 a")

# for i in result :
#     print(i.text)

time.sleep(2)

driver.close()