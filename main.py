from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://www.timeanddate.com/holidays/thailand/"
days = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0,
}

driver = webdriver.Firefox()
driver.get(URL)

rows = len(driver.find_elements("xpath", "//*[@id='holidays-table']/tbody/tr"))
columns = len(
    driver.find_elements(
        "xpath", "//*[@id='holidays-table']/tbody//tr[@class='showrow']"
    )
)

data = driver.find_elements(
    "xpath", "//*[@id='holidays-table']/tbody//tr[@class='showrow']"
)

for index in range(columns):
    day = data[index].text.split(" ")[2]
    for k, v in days.items():
        if day == k:
            days[k] += 1

print(days)
driver.close()
