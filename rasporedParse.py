from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import logging
from urllib.parse import urlparse
import time
logging.basicConfig(level=logging.DEBUG)

# Set up Firefox options to run in headless mode
options = Options()
# options.headless = True

# load username and password from file
with open('uname_pass.txt', 'r') as f:
    username = f.readline().strip().split(":")[1]
    password = f.readline().strip().split(":")[1]

# create a new Firefox browser instance
driver = webdriver.Firefox(options=options)

# Get the Selenium logger
logger = logging.getLogger('selenium')

# Create a file handler and set the log file path
log_file = 'selenium.log'
file_handler = logging.FileHandler(log_file)

# Configure the file handler
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add the file handler to the logger
logger.addHandler(file_handler)

# go to the login page
driver.get("https://osobnastranica.mcdonalds.hr/osobnaStranica/login")
# Find the login form
login_form = driver.find_element(By.CLASS_NAME, 'prijava')

# Find the username and password input fields within the form
username_input = login_form.find_element(By.ID, 'username')
password_input = login_form.find_element(By.ID, 'password')

# Enter the username and password
username_input.send_keys(username)
password_input.send_keys(password)
time.sleep(5)
# Submit the form to perform the login
login_form.submit()

# Wait for the page to load
driver.implicitly_wait(10)
time.sleep(5)
# now navigate to the 'raspored' page
driver.get("https://osobnastranica.mcdonalds.hr/osobnaStranica/raspored/rasporedRada/")
time.sleep(5)
# Get the page title
title = urlparse(driver.current_url).path.strip('/').split('/')[-1]

# Save the web page content to a separate HTML file
with open(f"{title}.html", "w") as f:
    f.write(driver.page_source)

# Quit the driver
driver.quit()
