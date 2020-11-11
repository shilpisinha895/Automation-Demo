from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import traceback
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome("/Webdriver path")
        driver.get("https://mytestingthoughts.com/Sample/home.html")
        driver.maximize_window()
        # First_name
        f_name = driver.find_element_by_name("first_name")
        f_name.send_keys("Abcdef")
        # Last_name
        l_name = driver.find_element_by_name("last_name")
        l_name.send_keys("xyz")
        # Gender
        male = driver.find_element_by_name('inlineRadioOptions').click()
        # Hobbies
        hobbies = driver.find_element_by_id("exampleFormControlSelect2")
        select = Select(hobbies)
        select.select_by_visible_text("Reading")
        # Department/office
        department = driver.find_element_by_name("department")
        select = Select(department)
        select.select_by_visible_text("Department of Engineering")
        # username
        user_name = driver.find_element_by_name("user_name")
        user_name.send_keys("user1234")
        # password
        pwd = driver.find_element_by_name("user_password")
        pwd.send_keys("abc_1234")
        # Confirm_password
        con_pwd = driver.find_element_by_name("confirm_password")
        con_pwd.send_keys("abc_1234")
        # E-mail
        email = driver.find_element_by_name("email")
        email.send_keys("abcdef.xyz@gmail.com")
        # Contact-no
        cont_no = driver.find_element_by_name("contact_no")
        cont_no.send_keys("123-456-7890")
        # AdditionalInfo
        ad_info = driver.find_element_by_id("exampleFormControlTextarea1")
        ad_info.send_keys("Abc is a good person")
        # Submit
        # submit_button = driver.find_element_by_class_name("btn-warning")
        submit_button = driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

    except (NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException) as e:
        print(str(e))
    except Exception as e:
        print("Some error occured"+ str(e))
        traceback.print_exc()
    finally:
        time.sleep(3)
        driver.quit()
