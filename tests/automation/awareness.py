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
        awareness_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/awareness"]'))
        )
        awareness_page.click()

        time.sleep(1)
        awareness_question_1= WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[3]/button[3]'))
        )
        awareness_question_1.click()

        # time.sleep(1)
        next_question_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[4]/button'))
        )
        next_question_button.click()

        # time.sleep(1)
        question_two = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[3]/button[3]'))
        )
        question_two.click()

        next_question_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[4]/button'))
        )
        next_question_button.click()

        question_three = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[3]/button[3]'))
        )
        question_three.click()

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