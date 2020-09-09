from selenium import webdriver
from getpass import getpass
import time
username = input("Enter Student ID: ")
password = getpass("Enter your password: ")
sub = int(input("How many subjects so you have: "))

def getSubjects(sub):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))

    qz = "gvCourseList_lblCourseCode_"

    subjectList = []

    for i in range(sub):
        iString = str(i)
        subjectList.append(qz+iString)
        elem = driver.find_element_by_id(subjectList[i]).get_attribute("innerHTML")
        print(elem)
def logout():
    #logout
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    signOut = driver.find_element_by_id("imgSignOut")
    signOut.click()


#driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
driver.get("https://vulms.vu.edu.pk/LMS_LandingPage.aspx")

username_textbox = driver.find_element_by_id("txtStudentID")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("txtPassword")
password_textbox.send_keys(password)
time.sleep(1)

login_button = driver.find_element_by_id("ibtnLogin")
login_button.click()


getSubjects(sub)

logout()