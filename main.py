#scheduling in shell

from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import time

url = 'https://fitness-academy.com.pl/kluby-fitness/wroclaw-maslicka/grafik-zajec#logowanie'
account = "Natalka"

# parser = argparse.ArgumentParser()
# parser.add_argument('xpath')
# parser.add_argument('account')
# args = parser.parse_args()

class BookClasses:
    def __init__(self, url):
        self.url = url

    def reserve(self, account) -> None:
        '''

        Flow:
        1. Connect to website
        2. Log in
            2.1 Access config file
            2.2 Input data into textboxes
        3. Select classes by Xpath

        '''

        driver = webdriver.Firefox()
        driver.get(url)

        # tu musimy przerzucić się na komunikat/strone do logowania, który występuje (co to wgl jest)

        config = ConfigParser()
        config.read("config.ini")
        login = config[account]["username"]
        password = config[account]["password"]

        popup_button = driver.find_element(By.ID, "didomi-notice-agree-button")
        popup_button.click()

        text_login = driver.find_element(By.ID, "member_login_form_email")
        text_login.clear()
        text_login.send_keys(login)

        text_password = driver.find_element(By.ID, "member_login_form_password")
        text_password.clear()
        text_password.send_keys(password)

        driver.find_element(By.ID, "member_login_form_submit").click()

        # wait = WebDriverWait(driver, 15)
        driver.implicitly_wait(10)

        print(driver.current_url)

        # TO NIE DZIAŁA BO JEST TO PSEUDO ELEMENT POTRZEBA JS
        pick_classes = driver.find_element(By.ID, "id") # wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
        pick_classes.click()

        print(driver.current_url)
        driver.implicitly_wait(10)

        for handle in driver.window_handles:
            driver.switch_to.window(handle)

        register_button = driver.find_element(By.ID, "schedule_register_form_submit") #wait.until(EC.element_to_be_clickable((By.ID, "schedule_register_form_submit")))
        register_button.click()

        print(driver.current_url)

        time.sleep(10)

        driver.close()

if __name__ == "__main__":
    classes = BookClasses(url) # tu później zmień na args.xpath
    classes.reserve(account) # tu zmien na args.account


