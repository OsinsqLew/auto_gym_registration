#scheduling in shell

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

url = 'https://fitness-academy.com.pl/kluby-fitness/wroclaw-maslicka/grafik-zajec'
#xpath do rezerwacji, login, password
def connect(url) -> bool:
    driver = webdriver.Chrome()
    driver.get(url)

def chose_classes():
    reserve = driver.find_element(By.XPATH, xpath) #chyba, że tego xpath da sie automatycznie generowac
    reserve.click()

def login():
    text_login = driver.find_element(By.ID, "member_login_form_email")
    text_login.clear()
    text_login.send_keys(login)

    text_password = driver.find_element(By.ID, "member_login_form_password")
    text_password.clear()
    text_password.send_keys(password)

    driver.find_element(By.ID, "member_login_form_submit").click()


driver.close()
