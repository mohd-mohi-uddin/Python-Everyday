from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


time.sleep(4)

# select_lang = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
# select_lang.click()