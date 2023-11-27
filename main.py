#scheduling in shell

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.actions import Actions
import argparse

url = 'https://fitness-academy.com.pl/kluby-fitness/wroclaw-maslicka/grafik-zajec'
#xpath do rezerwacji

parser = argparse.ArgumentParser()
args = parser.parse_args()

class BookClasses(xpath, url):
    def __init__(self, xpath):
        self.xpath = xpath

    def reserve(self): -> None:
    '''

        Flow:
        1. Connect to website
        2. Select classes by Xpath
        3. Log in
            3.1 Access config file
            3.2 Input data into textboxes

    '''
        driver = webdriver.Chrome()
        driver.get(url)

        reserve = driver.find_element(By.XPATH, self.xpath)  # chyba, że tego xpath da sie automatycznie generowac
        reserve.click()

        # tu musimy przerzucić się na komunikat/strone do logowania, który występuje



        # tu pobieramy z pliku config haslo i login


        text_login = driver.find_element(By.ID, "member_login_form_email")
        text_login.clear()
        text_login.send_keys(login)

        text_password = driver.find_element(By.ID, "member_login_form_password")
        text_password.clear()
        text_password.send_keys(password)

        driver.find_element(By.ID, "member_login_form_submit").click()

        driver.close()

if __name__ == __main__:
    classes = BookClasses()
    classes.reserve()

