# launch the browser
#open url
# find element by id/class
#perform action (click/type)
# verify result
# close browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from datetime import date, timedelta



def test_web_interaction():

    # Launch the browser
    driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)


    try:
        # Open URL
        driver.get("http://localhost:3000/")
        # driver.get("https://cleancityproject.netlify.app/")

        time.sleep(2)
        # move to the registration page
        # email = input("please enter your email:   ")

        # move to the registration page
        registration_nav = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/register"]'))
        )
        registration_nav.click()
        # enter name
        registration_name= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-name'))
        )
        registration_name.send_keys("John Doe")
        # enter the email
        registration_email= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-email'))
        )
        registration_email.send_keys("admin@cleancity.com")

        # enter the password for the new account
        registration_password= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-password'))
        )
        registration_password.send_keys("TestPass123")   ## registration password

        time.sleep(1.5)
        #submit the form by clicking
        registration_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        registration_button.click()
        #redirected to the login part
        login_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-email'))
        )
        # login_email.send_keys(f"{email}")
        login_email.send_keys("admin@cleancity.com")

        login_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-password'))
        )
        login_password.send_keys('38') ## new password
        time.sleep(1.5)
        login_button = WebDriverWait(driver, 15).until( 
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        login_button.click()
        
        dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard"]'))
        )
        dashboard.click()

        
        
    finally:
        # close browser
        input("Press Enter to exit..")
        driver.quit()

test_web_interaction()