from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
ACCOUNT_EMAIL = "mohi@test.com"
ACCOUNT_PASSWORD = "asim123@mohi"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

user_data_dir = os.path.join(BASE_DIR, "chrome_profile")
print(user_data_dir)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
