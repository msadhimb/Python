
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

def login():
    driver.get("https://kulino.dinus.ac.id/my/")
    
    username = driver.find_element_by_name("username")
    username.send_keys("a112012641")
    password = driver.find_element_by_name("password")
    password.send_keys("Dinus-03062002")
    username.send_keys(Keys.RETURN)
    absen()


def absen():    
    try:
        myclass = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "[20202] FISIKA 2"))
        )
        myclass.click()

        page = driver.find_element_by_id("page")
        print(page)

        myclass2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Absensi 30Juni 2021"))
        )
        myclass2.click()
        myclass3 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "30 Juni 2020"))
        )
        myclass3.click()
        myclass4 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Reply"))
        )
        myclass4.click()
        myclass5 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "post"))
        )
        myclass5.send_keys("Hadir")
        myclass6 = driver.find_element_by_css_selector("button.btn-primary")
        myclass6.click()
    except:
        pass

login()