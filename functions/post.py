import time
from selenium.webdriver.common.by import By

def make_post(driver, text):

    if driver.current_url != 'https://www.linkedin.com/feed/':
        driver.get('https://www.linkedin.com/feed/')

    driver.find_element(By.XPATH,"//span[text()='Start a post']/..").click()

    time.sleep(2)

    driver.find_element(By.XPATH, '//div[@data-placeholder="What do you want to talk about?"]').send_keys(text)

    time.sleep(2)

    driver.find_element(By.XPATH, '//span[text()="Post"]/..').click()

    time.sleep(2)