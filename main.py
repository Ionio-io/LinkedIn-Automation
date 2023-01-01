import time, json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.chrome.options import Options


from functions.login import linkedin_login


def load_cookies(driver, path):
    with open(path, 'r') as f:
        cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver


chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(60)

driver.get("https://www.linkedin.com/")

with open('cookies.json', 'r') as f:
    if len(f.readlines()) != 0:
        f.seek(0)
        cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)


linkedin_login(driver)


time.sleep(30)

driver.close()
