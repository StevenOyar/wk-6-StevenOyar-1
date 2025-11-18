# launch the browser
# open url
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

    driver.set_window_size(375, 812)


    try:
        # Open URL
        driver.get("http://localhost:3000/")
        # driver.get("https://cleancityproject.netlify.app/")

        
        # move to the registration page
        registration_nav = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/register"]'))
        )
        registration_nav.click()

        # 
        registration_name= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-name'))
        )
        registration_name.send_keys("John Doe")

        # 
        registration_email= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-email'))
        )
        registration_email.send_keys("admin@cleancity.com")
        
        # 
        registration_password= WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'register-password'))
        )
        registration_password.send_keys("TestPass123") 

        


        registration_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        registration_button.click()

        

        # email = input("please enter your email:   ")

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

        

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        login_button.click()

        
        # schedule pickup
        schedule_nav = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/home"]'))
        )
        schedule_nav.click()

        
        full_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-name'))
        )
        full_name.send_keys("John Doe")

        # 
        schedule_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-email'))
        )
        schedule_email.send_keys("user1@test.com")
        
        # 
        dropdown_location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "home-location"))
        )
        select = Select(dropdown_location)
        select.select_by_index(1)

        # 
        dropdown_waste_type = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "home-waste"))
        )
        select = Select(dropdown_waste_type)
        select.select_by_index(1)

        # 
        

         # Picking date
        pickup_date = (date.today() + timedelta(days=1)).strftime("%m-%d-%Y")

        date_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "home-date"))  
        )
        date_input.clear()
        date_input.send_keys(pickup_date)

        # 
        additonal_desc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'home-desc'))
        )
        additonal_desc.send_keys('Please do not forget this time')

        
        # submit the pick-up request
        submit_request = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_request.click()

        
        dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard"]'))
        )
        dashboard.click()

        
        blog_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/blog"]'))
        )
        blog_page.click()

        
        read_blog = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href="/blog/1"]' ))
        )
        read_blog.click()

        
        # testing adding comment to a blog
        add_comment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/section/div[2]/input'))
        )
        add_comment.send_keys("This is a great blog")
        

        comment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/section/div[2]/button'))
        )
        comment_button.click()

        
        like_comment = WebDriverWait(driver,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/section/div[1]/div/div/button[1]'))
        )
        like_comment.click()

        

        back_to_blog = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/blog"]'))
        )
        back_to_blog.click()

        
        # commnunity page
        community_page =WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/community"]'))
        )
        community_page.click()

        
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

        # 
        comment_in_community = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/form/textarea'))
        )
        comment_in_community.send_keys("London Project looks great the city is becoming clean")

        
        community_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        community_button.click()

        

        awareness_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/awareness"]'))
        )
        awareness_page.click()

        
        awareness_question_1= WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[3]/button[3]'))
        )
        awareness_question_1.click()

        # 
        next_question_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[4]/button'))
        )
        next_question_button.click()

        # 
        question_two = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[2]/div/div[3]/button[3]'))
        )
        question_two.click()

        
        report_button_awareness = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/section[4]/div/button[2]'))
        )
        report_button_awareness.click()


        # 
        request_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'feedback-request-id'))
        )
        request_id.send_keys("REQ-007")

        # 
        feedback = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'feedback-text'))
        )
        feedback.send_keys("the pickup was late but the driver was nice.")

        

        feedback_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        feedback_button.click()

        
        profile_nav = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/profile"]'))
        )
        profile_nav.click()

        # 

        profile_blog = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/button[1]'))
        )
        profile_blog.click()


        # 
        profile_comment = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/button[2]'))
        )
        profile_comment.click()

        # 
        profile_requests = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/button[3]'))
        )
        profile_requests.click()


        
        notification_bell = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/div/button'))
        )
        notification_bell.click()

        
        admin_profile = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/admin"]'))
        )
        admin_profile.click()

        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/button'))
        )
        logout_button.click()
    finally:
        # close browser
        input("Press Enter to exit..")
        driver.quit()

test_web_interaction()