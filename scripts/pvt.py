#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"/usr/bin/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service,options=options)
driver.get("https://workspaces.pexa.com.au/pexa_web/login.html")
element = driver.find_element(By.ID, "sign-in-link")
assert element.is_enabled()
print(element.is_enabled())

driver.quit()

print(driver.title)
