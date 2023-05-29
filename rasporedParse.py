from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlparse
import time
import os
import re
from RasporedClass import Raspored

def login(username, password):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)

    # Go to the login page
    driver.get("https://osobnastranica.mcdonalds.hr/osobnaStranica/login")

    # Find the login form
    login_form = driver.find_element(By.CLASS_NAME, 'prijava')

    # Find the username and password input fields within the form
    username_input = login_form.find_element(By.ID, 'username')
    password_input = login_form.find_element(By.ID, 'password')

    # Enter the username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Submit the form to perform the login
    div_element = login_form.find_element(By.CSS_SELECTOR, 'div.prijavaPanel.prijavaPanelLast')
    input_element = div_element.find_element(By.CSS_SELECTOR, 'input.uniInput.prijavaGumb')
    input_element.click()

    return driver

def save_page(driver):
    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the current page URL and extract the last part as the title
    title = urlparse(driver.current_url).path.strip('/').split('/')[-1]

    # Save the web page content to a separate HTML file
    with open(f"{title}.html", "w" , encoding="utf-8") as f:
        f.write(driver.page_source)

def get_raspored(driver):
    raspored_html = driver.find_element(By.ID, '1S').get_attribute('innerHTML')
    return extract_raspored(raspored_html)

def extract_raspored(raspored_html):
    # Extract the schedule
    time_cells = re.findall(r'<span class="dan_razdoblje".*?>(.*?)</span><span class="dan_ukupno".*?>(.*?)</span>', raspored_html)
    names = re.findall(r'<div class="tjedan_djelatnik" style="[^"]*" title="([^"]+)"[^>]*>[^<]*<\/div>', raspored_html)
    # Clean up the extracted data
    while ('Razdoblje', 'Sati') in time_cells:
        time_cells.remove(('Razdoblje', 'Sati'))
    for i in range(len(time_cells)):
        if time_cells[i] == ('&nbsp;', '&nbsp;'):
            time_cells[i] = ('none', 'none')
    return names[0] , time_cells
def write_csv(raspored):
    # Write the schedule to a CSV file
    pass

def main():
    with open('uname_pass.txt', 'r') as f:
        username = f.readline().strip().split(":")[1]
        password = f.readline().strip().split(":")[1]

    driver = login(username, password)

    # Now navigate to the 'raspored' page
    driver.get("https://osobnastranica.mcdonalds.hr/osobnaStranica/raspored/rasporedRada/")

    save_page(driver)
    write_csv(get_raspored(driver))
    raspored = Raspored(get_raspored(driver))
    # Quit the driver
    driver.quit()

def clean_before():
    # Remove all the files that were created by this script
    try:
            os.remove("login.html")
    except OSError:
        print("login.html does not exist")
    try:
            os.remove("rasporedRada.html")
    except OSError:
        print("rasporedRada.html does not exist")




if __name__ == "__main__":
    clean_before()
    main()
