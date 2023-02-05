import time, json

from selenium.webdriver.common.by import By

EMAIL = "pranaveatclub@gmail.com"
PASSWORD = "pranaveatclub@gmail.com123" #I changed the password, lol

def linkedin_login(driver):

    driver.get('https://www.linkedin.com/uas/login')

    time.sleep(2)

    if driver.current_url != 'https://www.linkedin.com/uas/login': return

    time.sleep(2)

    driver.find_element(By.ID, 'username').send_keys(EMAIL)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Sign in"]').click()

    with open('cookies.json', 'w') as f:
        json.dump(driver.get_cookies(), f)