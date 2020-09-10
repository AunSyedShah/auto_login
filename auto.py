from selenium import webdriver
from getpass import getpass
import sys
import time

# local variables
username = input("Enter Student ID: ")
password = getpass("Enter your password: ")



#driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
driver.get("https://vulms.vu.edu.pk/LMS_LandingPage.aspx")

def getSubjects():
    try:
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    except:
        sys.exit("Wrong Password or System Error")

    subjectList = []
    qz = "gvCourseList_lblCourseCode_"

    print("Subjects List\n==========")

    i = 0
    while(True):
        iString = str(i)
        subjectList.append(qz+iString)
        try:
            elem = driver.find_element_by_id(subjectList[i]).get_attribute("innerHTML")
            print(elem)
            i += 1
        except:
            break

def logout():
    #logout
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    signOut = driver.find_element_by_id("imgSignOut")
    signOut.click()
def login(username, password):
    username_textbox = driver.find_element_by_id("txtStudentID")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id("txtPassword")
    password_textbox.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element_by_id("ibtnLogin")
    login_button.click()
def calculateQuiz():
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    driver.find_element_by_id("gvCourseList_ibtnQuizzes_1_0").click()
    print("Quiz Grand Total")

    obtMarks = []
    obtMarksStr = "gvQuizList_lblGetMarks_"
    obtMarksString = ""
    count = 0
    while(True):
        obtMarksString = obtMarksStr + str(count)
        try:
            findQuiz = driver.find_element_by_id(obtMarksString).get_attribute("innerHTML")
            obtMarks.append(int(findQuiz))
            count += 1
        except:
            break
    print(sum(obtMarks))

login(username, password)
getSubjects()
calculateQuiz()
logout()