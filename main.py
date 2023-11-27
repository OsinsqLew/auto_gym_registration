#scheduling in shell

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import argparse

url = 'https://fitness-academy.com.pl/kluby-fitness/wroclaw-maslicka/grafik-zajec'
#xpath do rezerwacji, login, password

parser = argparse.ArgumentParser()
args = parser.parse_args()

class Book_Classes(xpath, url)
    def __init__(self, xpath):
        self.xpath = xpath

    def connect(url) -> None:
        driver = webdriver.Chrome()
        driver.get(url)

    def select_classes() -> None:
        reserve = driver.find_element(By.XPATH, xpath) #chyba, że tego xpath da sie automatycznie generowac
        reserve.click()

    def log_in() -> None:
        text_login = driver.find_element(By.ID, "member_login_form_email")
        text_login.clear()
        text_login.send_keys(login)

        text_password = driver.find_element(By.ID, "member_login_form_password")
        text_password.clear()
        text_password.send_keys(password)

        driver.find_element(By.ID, "member_login_form_submit").click()


driver.close()

if __name__ == __main__:
    classes = Book_Classes()
    classes.connect()
    classes.select_classes()
    classes.log_in()

