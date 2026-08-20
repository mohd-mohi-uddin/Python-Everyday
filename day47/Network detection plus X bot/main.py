from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 50
PROMISED_UP = 10
Y_EMAIL = os.environ.get("Y_EMAIL")
Y_PASSWORD = os.environ.get("Y_PASSWORD")

class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        wait = WebDriverWait(self.driver, 40)

        privacy_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))

        self.driver.execute_script(
            "arguments[0].click();",
            privacy_button
        )

        go_button = wait.until(ec.element_to_be_clickable((
            By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
            ))
        )

        go_button.click()

        down_result_page = wait.until(ec.presence_of_element_located(
            (
                By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]'
            )
        ))

        wait.until(
            lambda driver: down_result_page.find_element(By.XPATH, ".//h3").text != "—"
        )

        down = down_result_page.find_element(By.XPATH, ".//h3").text


        up_result_div = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div')))

        wait.until(
            lambda driver: up_result_div.find_element(By.XPATH, ".//h3").text != "—"
        )

        up = up_result_div.find_element(By.XPATH, ".//h3").text

        return float(down), float(up)


    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y")

        wait = WebDriverWait(self.driver, 40)

        cookie_button = wait.until(ec.element_to_be_clickable((
            By.XPATH, '//*[@id="y-cookie-banner"]/button'
        )))
        cookie_button.click()

        login_button = self.driver.find_element(By.XPATH, value= '/html/body/div/div[1]/a[4]')
        login_button.click()

        enter_email = wait.until(ec.presence_of_element_located((By.ID, "email")))
        enter_email.send_keys(Y_EMAIL)

        enter_password = wait.until(ec.presence_of_element_located((By.ID, "password")))
        enter_password.send_keys(Y_PASSWORD)

        second_login = wait.until(ec.element_to_be_clickable((
            By.XPATH, '/html/body/div/div/form/button'
        )))
        second_login.click()

        enter_tweet = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="tweet-compose"]')))
        enter_tweet.send_keys(f"@comcast, hey comcast my internet speed today is (down:{down}mbps,up:{up}mbps), you promised to gave (down:{PROMISED_DOWN}mbps,up:{PROMISED_UP}mbps) internet speed. i want you to fix this soon.")

        post_button= wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="post-btn"]')))
        post_button.click()

bot = InternetSpeedTwitterBot()
down, up = bot.get_internet_speed()
print(up, down, type(up), type(down))
if PROMISED_DOWN > down or PROMISED_UP > up:
    bot.tweet_at_provider()