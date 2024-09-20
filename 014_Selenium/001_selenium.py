from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.FireFox()

url = "https://www.google.com/"
driver.get(url)
