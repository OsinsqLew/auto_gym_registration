#scheduling in shell

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import argparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser
import time

url = 'https://fitness-academy.com.pl/kluby-fitness/wroclaw-maslicka/grafik-zajec'

parser = argparse.ArgumentParser()
parser.add_argument('account')
args = parser.parse_args()

class BookClasses:
    def __init__(self, url):
        self.url = url

    def reserve(self, account) -> None:
        '''

        Flow:
        1. Connect to website
        2. Go to reservation site
            2.1 Find classes by xpath and get link to reservation
            2.2 Switch to reservation site
        3. Reserve Classes
            3.1 Log in
                3.1.1 Access config file
                3.1.2 Input data into textboxes
            3.2 Submit

        '''

        driver = webdriver.Firefox()
        driver.get(self.url)

        config = ConfigParser()
        config.read("config.ini")
        login = config[account]["username"]
        password = config[account]["password"]
        xpath = config[account]["xpath"]

        driver.implicitly_wait(30)

        popup_button = driver.find_element(By.ID, "didomi-notice-agree-button")
        popup_button.click()

        pick_classes = driver.find_element(By.XPATH, xpath)
        href = pick_classes.get_attribute("href")

        driver.get(href)

        register_button = driver.find_element(By.ID, "schedule_register_form_submit")
        register_button.click()

        text_login = driver.find_element(By.ID, "member_login_form_email")
        text_login.clear()
        text_login.send_keys(login)

        text_password = driver.find_element(By.ID, "member_login_form_password")
        text_password.clear()
        text_password.send_keys(password)

        driver.find_element(By.ID, "member_login_form_submit").click()

        wait = WebDriverWait(driver, 10)
        time.sleep(10)

        schedule_button = driver.find_element(By.ID, "schedule_register_form_submit")
        wait.until(EC.element_to_be_clickable((By.ID, "schedule_register_form_submit")))

        schedule_button.submit()

        time.sleep(10)

        driver.close()

if __name__ == "__main__":
    classes = BookClasses(url)
    classes.reserve(args.account)


