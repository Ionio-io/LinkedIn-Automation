import time
from selenium.webdriver.common.by import By


def like_post(driver, post_url):
    
    driver.get(post_url)

    time.sleep(2)
    
    driver.find_element(By.XPATH ,"//span[text()='Like']").click()

    time.wait(1)