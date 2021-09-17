from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


def click(driver, element):
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, element))
    )
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, element))
    )
    driver.find_element_by_css_selector(element).click()

def clickclass(driver, element):
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, element))
    )
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CLASS_NAME, element))
    )
    driver.find_element_by_class_name(element).click()

timerH = int(input('Masukkan jam : '))
timerM = int(input('Masukkan menit : '))
timerS = int(input('Masukkan detik : '))
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


while True:
    if timerH == datetime.datetime.now().hour and timerM == datetime.datetime.now().minute and timerS == datetime.datetime.now().second:
        driver.refresh()
        myclass = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Infinix Note 10 4/64GB - Helio G85 - 6.95inch FHD+ 90 Hz - 48MP Triple Camera 95 Black"))
                    )
                    
        myclass.click()
        click(driver, "button.btn.btn-solid-primary.btn--l._3Kiuzg")
        WebDriverWait(driver, 21).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".action-toast")))
        clickclass(driver, "shopee-button-solid.shopee-button-solid--primary")
        WebDriverWait(driver, 21).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".loading-spinner-popup")))
        clickclass(driver, "stardust-button.stardust-button--primary.stardust-button--large._1qSlAe")