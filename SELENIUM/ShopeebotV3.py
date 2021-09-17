from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import WEBDRIVER_EXT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


def click(driver, element):
    WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, element))
    )
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, element))
    )
    driver.find_element_by_css_selector(element).click()

linkproduk = input('Masukkan link : ')
timerH = int(input('Masukkan jam : '))
timerM = int(input('Masukkan menit : '))
timerS = int(input('Masukkan detik : '))

path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get(linkproduk)

myclass = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div._193wCc > div.shopee-top.container-wrapper > div.navbar-wrapper.container-wrapper > div > ul > a:nth-child(5)"))
)
myclass.click()

username = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.NAME, "loginKey"))
)
username.send_keys("0895364594801")
password = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password.send_keys("Salatiga123")
password.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 60)

while True:
    if timerH == datetime.datetime.now().hour and timerM == datetime.datetime.now().minute and timerS == datetime.datetime.now().second:
        driver.refresh()
        click(driver, "button.btn.btn-solid-primary.btn--l._3Kiuzg")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.action-toast')))
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.action-toast')))
        
        click(driver, ".shopee-button-solid")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.loading-spinner-popup')))
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loading-spinner-popup')))
        
        click(driver, ".stardust-button")

