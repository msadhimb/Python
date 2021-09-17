from logging import log
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def timer():
    global timerH
    global timerM
    global timerS
    global waktu

    timerH = int(input('Masukkan jam : '))
    timerM = int(input('Masukkan menit : '))
    timerS = int(input('Masukkan detik : '))
    waktu = input('am / pm ?')
    
    login()

def login():
    global path
    global driver

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2Fflash_sale%3FpromotionId%3D2016525492&promotionId=2016525492")

    username = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.NAME, "loginKey"))
)
    username.send_keys("0895364594801")
    password = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
    password.send_keys("Salatiga123")
    password.send_keys(Keys.RETURN)
    execute()

def execute():
    while True:
        if timerH == datetime.datetime.now().hour and timerM == datetime.datetime.now().minute and timerS == datetime.datetime.now().second:
                driver.refresh()
                myclass = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Infinix Note 10 4/64GB - Helio G85 - 6.95inch FHD+ 90 Hz - 48MP Triple Camera 95 Black"))
            )
            
                myclass.click()
                asu()
    
def asu():
                myclass = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-solid-primary.btn--l._3Kiuzg"))
            )
                myclass.click()
                WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".action-toast")))
                logok()
    
def logok():
                myclass = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopee-button-solid.shopee-button-solid--primary"))
            )
                myclass.click()
                WebDriverWait(driver, 60).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".loading-spinner-popup")))
                bajigan()

def bajigan():
                myclass = WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.PC1-mc > div._3Q9F5R._1Q3ggw > button"))
            )   
                myclass.click()

           

timer()