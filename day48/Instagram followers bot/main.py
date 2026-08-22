from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

LOGIN_EMAIL = "mohdmohiuddin1409@gmail.com"
LOGIN_PASSWORD = "4LsO4aRfM7H7al0H"

class SendANaanBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options= self.chrome_options)

    def follow_accounts(self):
        self.driver.get("https://app.100daysofpython.dev/services/share-a-naan/welcome")

        wait = WebDriverWait(self.driver,15)

        enter_email = wait.until(ec.presence_of_element_located((By.XPATH,'/html/body/div/aside/div/form/input[1]')))
        enter_email.send_keys(LOGIN_EMAIL)

        enter_password = wait.until(ec.presence_of_element_located((By.XPATH,'/html/body/div/aside/div/form/input[2]')))
        enter_password.send_keys(LOGIN_PASSWORD)  

        login_button = wait.until(ec.element_to_be_clickable((
            By.XPATH,'/html/body/div/aside/div/form/button'
        )))
        login_button.click()

        not_now_button = wait.until(ec.element_to_be_clickable((
            By.XPATH, '//*[@id="popup-save-login"]/div/div[2]'
        )))
        not_now_button.click()

        again_not_now_button = wait.until(ec.element_to_be_clickable((
            By.XPATH, '//*[@id="popup-notifications"]/div/button[2]'
        )))
        again_not_now_button.click()

        search = wait.until(ec.element_to_be_clickable((
            By.XPATH, '/html/body/div[1]/nav/button'
        )))
        search.click()

        chef_steps = wait.until(ec.presence_of_element_located((
            By.XPATH,'/html/body/aside/div[4]/a[1]'
        )))
        chef_steps.click()

        click_followers = wait.until(ec.presence_of_element_located((
            By.XPATH,'/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a'
        )))
        click_followers.click()

        wait.until(ec.presence_of_element_located((
            By.XPATH, '/html/body/div[2]/div/div[3]'
        )))

        followers_list = self.driver.find_elements(By.CLASS_NAME, value="naan-follower-row")
        if followers_list:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", followers_list[-1])
        for follower in followers_list:
            button = follower.find_element(By.TAG_NAME, value="button")
            if button.text == "Follow":
                button.click()
            
bot = SendANaanBot()
bot.follow_accounts()

#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options= chrome_options)
#     driver.get("https://workspace.google.com/intl/en-US/gmail/")

#     wait = WebDriverWait(driver,20)

#     sign_in_button = wait.until(ec.element_to_be_clickable((
#         By.XPATH, '//*[@id="root"]/gws-header/header/div/div[3]/span[3]/a/span'
#     )))
#     sign_in_button.click()

#     wait.until(lambda driver: len(driver.window_handles)>1)

#     driver.switch_to.window(driver.window_handles[-1])

#     enter_email = wait.until(ec.presence_of_element_located((By.ID, "identifierId")))
#     enter_email.send_keys(LOGIN_EMAIL)

#     click_next = wait.until(ec.element_to_be_clickable((
#         By.XPATH, '//*[@id="identifierNext"]/div/button/span'
#     )))
#     click_next.click()

# get_code()

# class InstagramFollowersBot:

#     def __init__(self):
#         self.chrome_options = webdriver.ChromeOptions()
#         self.chrome_options.add_experimental_option("detach", True)
#         self.driver = webdriver.Chrome(options= self.chrome_options)

#     def instagram_login(self):
#         self.driver.get("https://www.instagram.com/accounts/login/?hl=en")

#         wait = WebDriverWait(self.driver,10)

#         enter_email = wait.until(ec.presence_of_element_located((
#             By.XPATH, '//*[@id="_R_32d9lplcldcpbn6b5ipamH1_"]'
#             ))
#         )
#         enter_email.send_keys(LOGIN_EMAIL)

#         enter_password = self.driver.find_element(By.XPATH, '//*[@id="_R_33d9lplcldcpbn6b5ipamH1_"]')
#         enter_password.send_keys(LOGIN_PASSWORD)

#         login_button = wait.until(ec.element_to_be_clickable((
#             By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]'
#             ))
#         )
#         login_button.click()




# bot = InstagramFollowersBot()
# bot.instagram_login()