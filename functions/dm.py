import time
from selenium.webdriver.common.by import By


def send_message(driver, user_url, message):
    driver.get(user_url)

    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[text()="Message"]')

    if element.tag_name != "a": return driver #STOP EXECUTION IF WE CANNOT SEND MESSAGES TO THE USER

    driver.get(element.get_attribute('href'))

    time.sleep(2)

    #NOW WE ARE ON THE DMs page

    driver.find_element(By.XPATH, "//div[@aria-label='Write a message…']").send_keys(message)

    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Send']").click()