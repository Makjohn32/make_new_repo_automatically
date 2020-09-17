from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
 
PATH = "C:/Program Files (x86)/msedgedriver.exe"
driver = webdriver.Edge(PATH)

#Log in in github account
driver.get("https://github.com/login")
username = driver.find_element_by_id("login_field")
username.click()
username.send_keys("makjohn32@gmail.com")
password = driver.find_element_by_id("password")
password.click()
password.send_keys("3264Projects")
password.send_keys(Keys.RETURN)

#create a new repository

driver.get("https://github.com/new")
new_repo_name = driver.find_element_by_id("repository_name")
name = str(input("Give the name of the repository:"))
new_repo_name.send_keys(name)
add_readme = driver.find_element_by_id("repository_auto_init")
add_readme.click()
create_repo_button = driver.find_element_by_css_selector("button.first-in-line")
create_repo_button.submit()