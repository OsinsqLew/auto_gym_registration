#checking time
import schedule
from datetime import time

begin_time = time(hour= , minute= ,second= )
schedule.every().friday.at(begin_time).do(connect) # ew trzeba będzie zmienić dzień 
schedule.every().friday.at(begin_time).do(book)

#connect to website
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
# By class is used to locate elements within a document

def connect(url) -> bool:
    driver = webdriver.Firefox()
    driver.get(url)

    element = driver.find_element(By., )
    element.clear( ) # czyści jeśli coś jest wcześniej wpisane w okienko

    element.send_keys(Keys.ENTER) # wciska klawisz, można to robić na każdym elem dzięki czemu można stosować skróty klawiszowe
    driver.find_element(By.ID, "submit").click() # klika przycisk
    driver.close()


#booking
def book():
    pass()