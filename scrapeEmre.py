from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
driver = webdriver.Chrome(desired_capabilities=caps, executable_path="path/to/chromedriver.exe")

for ilInd in range(1, 81):
    
    ilInd = str(int(ilInd))
    driver.get('https://sts.chp.org.tr')

    WebDriverWait(driver, timeout=10).until(
        ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
    )

    driver.find_element(By.ID, "rdveriKaynagi_1").click()

    il = Select(driver.find_element(By.ID, 'ddlIller'))
    il.select_by_index(ilInd)
    il_name = driver.find_element(By.ID, 'ddlIller').get_attribute('value')
    time.sleep(1)

    ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
    ilceOptions = ilce.options
    toplamIlce = len(ilceOptions)
    ilce.select_by_index('1')
    time.sleep(1)

    sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
    sandikOptions = sandik.options
    toplamSandik = len(sandikOptions)
    print(toplamSandik)


    for ilceInd in range(1, toplamIlce):
        for sandikInd in range(1,toplamSandik):

            driver.get('https://sts.chp.org.tr')

            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
            )

            driver.find_element(By.ID, "rdveriKaynagi_1").click()

            il = Select(driver.find_element(By.ID, 'ddlIller'))
            il.select_by_index(ilInd)
            il_name = driver.find_element(By.ID, 'ddlIller').get_attribute('value')
            time.sleep(1)

            ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
            ilce.select_by_index(ilceInd)
            ilce_name = driver.find_element(By.ID, 'ddlIlceler').get_attribute('value')
            time.sleep(1)

            sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
            sandik.select_by_index(str(sandikInd))
            sandik_no = driver.find_element(By.ID, 'ddlSandiklar').get_attribute('value')
            
            driver.find_element(By.ID, "btnSorgula").click()
            time.sleep(1)

            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )

            MVvote = []

            print(driver.find_element(By.ID, "txtCHP").get_attribute('value'))
            #MVvote.append( driver.find_element(By.ID, "txtCHP").get_attribute('value') )
            #MVvote.append( driver.find_element(By.ID, "txtAKP").get_attribute('value') )
            #MVvote.append( driver.find_element(By.ID, "txtIyi").get_attribute('value') )
            #MVvote.append( driver.find_element(By.ID, "txtYesilSol").get_attribute('value') )
            #MVvote.append( driver.find_element(By.ID, "txtMhp").get_attribute('value') )

            print(MVvote)

            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )
            driver.find_element(By.ID, "btnCb").click()

            vote = []

            vote.append(driver.find_element(By.ID, "txtCB1").get_attribute('value'))
            vote.append(driver.find_element(By.ID, "txtCB2").get_attribute('value'))
            vote.append(driver.find_element(By.ID, "txtCB3").get_attribute('value'))
            vote.append(driver.find_element(By.ID, "txtCB4").get_attribute('value'))

            print(vote)
