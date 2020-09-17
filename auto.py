from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options
from os import system
import sys
import time

def loadDriver(state = 1):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    #driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
    try:
        if state == 1:
            driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe", options=option)
        else:
            driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
        return driver
    except:
        sys.exit("You don't have chrome Installed")
def getSubjects(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgLMSHome").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    subjectList = []

    qz = "gvCourseList_lblCourseCode_"

    i = 0
    while(True):
        iString = str(i)
        try:
            subjectList.append(driver.find_element_by_id(qz+iString).get_attribute("innerHTML"))
            i += 1
        except:
            break
    return subjectList
def logout(driver):
    #logout
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    signOut = driver.find_element_by_id("imgSignOut")
    signOut.click()
    print("Logged Out")
# returns true if successful login
def login(username, password, driver):

    username_textbox = driver.find_element_by_id("txtStudentID")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id("txtPassword")
    password_textbox.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element_by_id("ibtnLogin")
    login_button.click()

    # login status check
    try:
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_name("header"))
        system("cls")
        print("\nLogin Successful")
        return True
    except:
        return False
# returns a string
def getStudDetail(driver):
    details = []
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgProfile").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    #list append
    details.append(str(driver.find_element_by_id("lblStdName").get_attribute("innerHTML")))
    details.append(str(driver.find_element_by_id("lblVuEmail").get_attribute("innerHTML")))
    details.append(str(driver.find_element_by_id("lblStudyPro").get_attribute("innerHTML")))
    details.append(str(driver.find_element_by_id("lblCurSemester").get_attribute("innerHTML")))
    return details
def calculateQuiz(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgLMSHome").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    driver.find_element_by_id("gvCourseList_ibtnQuizzes_1_0").click()
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
    return sum(obtMarks)
def calculateAssignment(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgLMSHome").click()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    driver.find_element_by_id("gvCourseList_ibtnAssignments_1_0").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    driver.switch_to.frame(driver.find_element_by_id("ifrmAssignmentsArea"))
    obtMarks = 0
    count = 0
    while(True):
        try:
            driver.switch_to.frame(driver.find_element_by_id("ifrmAssignmentsArea"))
            #driver.switch_to.frame(driver.find_element_by_name("ifrmAssignmentsArea"))
            findAssignment = float(driver.find_element_by_id("gvStdAssign_lblScore_" + str(count)).get_attribute("innerHTML"))
            obtMarks += findAssignment
            count += 1
        except:
            break
    return obtMarks
def calculateGDB(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgLMSHome").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    driver.find_element_by_id("gvCourseList_ibtnGDB_1_0").click()
    obtMarks = []
    obtMarksStr = "grdGDBs_lblMarksObtained_"
    obtMarksString = ""
    count = 0
    while(True):
        obtMarksString = obtMarksStr + str(count)
        try:
            findQuiz = driver.find_element_by_id(obtMarksString).get_attribute("innerHTML")
            obtMarks.append(float(findQuiz))
            count += 1
        except:
            break
    return sum(obtMarks)

def getTotalPayable(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgAccountBook").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    fee_due = driver.find_element_by_id("grdaccountbook_lblTotalPayableBalace").get_attribute("innerHTML")
    return fee_due
def getQuizPercentage(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    print((calculateQuiz(driver) / 50) * 20)
# returns integer value
def totalAmountPaid(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("header"))
    driver.find_element_by_id("imgAccountBook").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("frmContents"))
    i = 0
    sum = 0
    while(True):
        try:
            sum += int(driver.find_element_by_id("grdaccountbook_lblPaidAmount_" + str(i)).get_attribute("innerHTML"))
            i += 1
        except:
            break
    return sum
def main():
    # local variables
    system("cls")
    print("Console based VULMS\n==========")
    username = input("Enter Student ID: ")
    password = getpass("Enter your password: ")
    url = "https://vulms.vu.edu.pk/LMS_LandingPage.aspx"

    system("cls")

    print("System is Working, Please Wait\n")
    # function calls
    driver = loadDriver(0)
    driver.get(url)

    system("cls")

    login_status = login(username, password, driver)
    if login_status:
        subjects = getSubjects(driver)
        fee_due = getTotalPayable(driver)
        amount_paid = totalAmountPaid(driver)
        detail = getStudDetail(driver)
        assgn = calculateGDB(driver)

        while(True):
            print("Welcome " + detail[0])
            print("This is Your Data")
            print("Email: " + detail[1])
            print("Study Program: " + detail[2])
            print("Semester Program: " + detail[3])
            print("1. View Your Subjects")
            print("2. Account Book")
            print("3. Amount Paid")
            print("4. Logout")
            print("GDB Total {0}".format(assgn))
            userChoice = int(input("What do you want to do: "))

            system("cls")

            if userChoice == 1:
                print("\nSubject List\n==========")
                for subject in subjects:
                    print(subject)
            elif userChoice == 2:
                print("Account Book")
                print("You have to pay " + fee_due)
            elif userChoice == 3:
                print("You Paid " + str(amount_paid) + " in total till now")
            elif userChoice == 4:
                logout(driver)
                break
            #calculateQuiz(driver)
            #logout(driver)
            system("pause")
            system("cls")
        sys.exit("You may close the window")
    else:
        sys.exit("Wrong Password")
if __name__ == "__main__":
    main()