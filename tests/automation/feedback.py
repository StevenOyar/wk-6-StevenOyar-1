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
        login_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/login"]'))
        )
        login_page.click()

        time.sleep(2)
        #redirected to the login part
        login_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-email'))
        )
        # login_email.send_keys(f"{email}")
        login_email.send_keys("admin@cleancity.com")

        # 

        login_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-password'))
        )
        login_password.send_keys('TestPass123')
        time.sleep(2)
        #submit the details 
        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        login_button.click()

        time.sleep(1)
        # navigate to the dashboard to see
        dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard"]'))
        )
        dashboard.click()

        time.sleep(1)

        #feedback page
        feedback_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href="/feedback"]'))
        )
        feedback_page.click()
        time.sleep(2)
        # request id
        request_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'feedback-request-id'))
        )
        request_id.send_keys("REQ-007")
        time.sleep(2)
        # 
        feedback = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'feedback-text'))
        )
        feedback.send_keys("the pickup was late but the driver was nice.")
        time.sleep(2)
        feedback_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        feedback_button.click()

        
        time.sleep(1)
         # navigate to the dashboard to see
        dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard"]'))
        )
        dashboard.click()


    finally:
        # close browser
        input("Press Enter to exit..")
        driver.quit()

test_web_interaction()