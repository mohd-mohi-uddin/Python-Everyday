from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

time.sleep(2)

first_name = driver.find_element(By.NAME, value= "fName")
first_name.send_keys("mohi")

last_name = driver.find_element(By.NAME, value= "lName")
last_name.send_keys("don")

email = driver.find_element(By.NAME, value= "email")
email.send_keys("mohidon@gmail.cum")

signup = driver.find_element(By.XPATH, value= '//*[@id="signup-form"]/button')
signup.click()



