"""

This project was made specifically  for accessing Stack Overflow using Google Chrome!

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path


# Download the driver on https://pypi.org/project/selenium/
# Configure the path to match your chromedriver.exe path, in my project the .exe is on the same file as main.py
ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver.exe'


class ChromeAccess:
    def __init__(self):
        self.chrome_service = Service( executable_path=str( CHROME_DRIVER_PATH ) )
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome( service=self.chrome_service , options=self.chrome_options )

    def login_click(self):
        try:
            btn_login = self.chrome.find_element(By.LINK_TEXT, 'Log-in')
            btn_login.click()
        except Exception as e:
            print('Error login_click(): ', e)

    def login(self, email, pw):
        try:
            email_field = self.chrome.find_element(By.ID, 'email')
            pw_field = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.ID, 'submit-button')

            email_field.send_keys(email)
            pw_field.send_keys(pw)
            sleep(2)
            btn_login.click()
        except Exception as e:
            print('Error login(): ', e)

    def dropdown_menu_click(self):
        try:
            dropdown_icon = self.chrome.find_element(By.CSS_SELECTOR, 'body > header > div > ol > li:nth-child(7) > a')
            dropdown_icon.click()
        except Exception as e:
            print('Error profile_icon_click(): ', e)

    def logout(self):
        try:
            btn_logout = self.chrome.find_element(By.CSS_SELECTOR, 'body > header > div > ol > li:nth-child(8) > div > div.modal-content.bg-powder-050.current-site-container > ul > li:nth-child(1) > div.related-links > a:nth-child(3)')
            btn_logout.click()
        except Exception as e:
            print('Error logout(): ', e)

    def logout_again(self):
        try:
            btn_logout = self.chrome.find_element(By.CSS_SELECTOR, '#content > div > form > div.d-flex.gs4 > button')
            btn_logout.click()
        except Exception as e:
            print('Error logout_again(): ', e)

    def access(self, site):
        self.chrome.get(site)

    def quit(self):
        self.chrome.quit()


if __name__ == '__main__':
    # The e-mail of your stack overflow account
    login_email = ''
    # The password of your stack overflow account
    login_pw = ''

    if login_email != '' and login_pw != '':
        browser = ChromeAccess()
        browser.access('https://pt.stackoverflow.com/')
        browser.login_click()
        browser.login(login_email, login_pw)
        sleep(3)
        browser.dropdown_menu_click()
        sleep(2)
        browser.logout()
        sleep(2)
        browser.logout_again()

        sleep(6)
        browser.quit()
    else:
        print('You forgot to put your email and/or password!')
