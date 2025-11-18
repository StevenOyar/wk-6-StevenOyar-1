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
        # commnunity page
        community_page =WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/community"]'))
        )
        community_page.click()

         # 
        comment_in_community = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/form/textarea'))
        )
        comment_in_community.send_keys("London Project looks great the city is becoming clean")

        
        community_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        community_button.click()

        # like the commnuity posts
        # like first post
        time.sleep(1)
        first_like = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/section/div/article[1]/div[2]/button[1]')
            )
        )
        first_like.click()

        second_like = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/section/div/article[2]/div[2]/button[1]')
            )
        )
        second_like.click()
        time.sleep(1)
        like_admin_community = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/section/div/article[3]/div[2]/button[1]')
            )
        )
        like_admin_community.click()

        # click to comment on admin comment
        # 
        comment_admin_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  '//*[@id="root"]/div/div/div/section/div/article[3]/div[2]/button[2]'))
        )
        comment_admin_button.click()

        # comment on the admin post
        # 
        comment_admin_comment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/section/div/article[3]/div[3]/form/input'))
        )
        comment_admin_comment.send_keys("My street also look clean after clear")

        
        # comment_button_ under the admin post
        subcomment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section/div/article[3]/div[3]/form/button'))
        )
        subcomment_button.click()

       
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