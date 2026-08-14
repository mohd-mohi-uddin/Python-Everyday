from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
dates_list = []
for date in dates:
    dates_list.append(date.text)
print(dates_list)

events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
events_list = []
for event in events:
    events_list.append(event.text)

events_dict = {}

for n in range(len(events_list)):
    events_dict[n] = {
        "date" : dates_list[n],
        "name" : events_list[n]
    }

print(events_dict)
driver.close()


