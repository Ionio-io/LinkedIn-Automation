import time
from selenium.webdriver.common.by import By


def send_message(driver, user_url):
    driver.get(user_url)

    time.sleep(2)

    