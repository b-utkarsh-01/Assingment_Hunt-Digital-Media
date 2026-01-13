from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
import os

# Random credentials
email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Edge setup
options = Options()
options.add_argument("--start-maximized")

driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

# Open login page
driver.get("http://127.0.0.1:8000/login")

wait = WebDriverWait(driver, 30)

# 🔥 Robust locators (works even if attributes change)
email_input = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'Email') or contains(@name,'email') or @type='email']")
    )
)

password_input = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'Password') or contains(@name,'password') or @type='password']")
    )
)

email_input.send_keys(email)
password_input.send_keys(password)

time.sleep(3)
driver.quit()
