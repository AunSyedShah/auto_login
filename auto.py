# thats private Brance
from selenium import webdriver
from getpass import getpass
import time
username = input("Enter Student ID: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
driver.get("https://vulms.vu.edu.pk/LMS_LandingPage.aspx")

username_textbox = driver.find_element_by_id("txtStudentID")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("txtPassword")
password_textbox.send_keys(password)
time.sleep(10)

login_button = driver.find_element_by_id("ibtnLogin")
login_button.click()
