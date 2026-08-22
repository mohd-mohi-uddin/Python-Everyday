from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

#BEAUTIFUL SOAP
#This peice of code is written to extract details of house rent using beautiful soap


response  = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html = response.text

soup = BeautifulSoup(html, "html.parser")

price_list = []
address_list = []
link_list = []

price_tags = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
for tag in price_tags:
    price_list.append(tag.text.split("+")[0])

address_tags = soup.find_all("address")
for tag in address_tags:
    address_list.append(tag.text.split("                                  ")[1].split("\n")[0])

link_tags = soup.select(".StyledPropertyCardDataWrapper a")
for tag in link_tags:
    link_list.append(tag.get("href"))


#SELENIUM WEBDRIVER
#This code is written to enter the details into the google sheets using selenium.

def add_detals(sno,price,address,link):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSflogjjja8VLXLpakBB2wc3QDLpI4seO6FWIrroPjRzMu4-yA/viewform?usp=header")

    wait = WebDriverWait(driver,15)

    price_input = wait.until(ec.presence_of_element_located((
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ))
    )
    price_input.send_keys(price)

    address_input = wait.until(ec.presence_of_element_located((
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ))
    )
    address_input.send_keys(address)

    link_input = wait.until(ec.presence_of_element_located((
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ))
    )
    link_input.send_keys(link)

    submit_button = wait.until(ec.element_to_be_clickable((
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    )))
    submit_button.click()

    driver.close()

    print(f"{sno}.added: {price}, {address}, {link}")



for i in range(len(price_list)):
    add_detals(i,price_list[i],address_list[i],link_list[i])
    time.sleep(2)
