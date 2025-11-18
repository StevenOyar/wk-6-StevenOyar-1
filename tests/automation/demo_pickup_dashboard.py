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

        
        # schedule pickup page nav gate
        schedule_nav = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/home"]'))
        )
        schedule_nav.click()
        # full name input
        full_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-name'))
        )
        full_name.send_keys("John Doe")
        #email input
        schedule_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-email'))
        )
        schedule_email.send_keys("user1@test.com")
        #choose the location from the drop down
        dropdown_location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "home-location"))
        )
        select = Select(dropdown_location)
        select.select_by_index(1)
        #choose the waste type from the dropdown
        dropdown_waste_type = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "home-waste"))
        )
        select = Select(dropdown_waste_type)
        select.select_by_index(1)
         # Picking date 
        pickup_date = (date.today() + timedelta(days=1)).strftime("%m-%d-%Y")
        date_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "home-date"))  
        )
        date_input.clear()
        date_input.send_keys(pickup_date)
        # sample of the description optional
        additonal_desc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-desc'))
        )
        additonal_desc.send_keys('Please do not forget this time')
        time.sleep(2)
        # submit the pick-up request
        submit_request = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_request.click()
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