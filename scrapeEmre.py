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

for ilInd in range(1,81):
    
    ilInd = str(int(ilInd))
    driver.get('https://sts.chp.org.tr')

    WebDriverWait(driver, timeout=100).until(
        ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
    )

    driver.find_element(By.ID, "rdveriKaynagi_1").click()
    

    WebDriverWait(driver, timeout=20).until(
        ec.visibility_of_element_located((By.ID, "ddlIller"))
    )
    il = Select(driver.find_element(By.ID, 'ddlIller'))
    il.select_by_index(ilInd)
    il_name = driver.find_element(By.ID, 'ddlIller').get_attribute('value')
    time.sleep(1)

    WebDriverWait(driver, timeout=20).until(
        ec.visibility_of_element_located((By.ID, "ddlIlceler"))
    )
    ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
    ilceOptions = ilce.options
    toplamIlce = len(ilceOptions)
    ilce.select_by_index('1')
    time.sleep(1)
    
    driver.find_element(By.ID, "btnSorgula").click()


    WebDriverWait(driver, timeout=20).until(
        ec.visibility_of_element_located((By.ID, "ddlSandiklar"))
    )
    sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
    sandikOptions = sandik.options
    toplamSandik = len(sandikOptions)

    for ilceInd in range(1, toplamIlce):
        for sandikInd in range(1,toplamSandik):

            driver.get('https://sts.chp.org.tr')

            WebDriverWait(driver, timeout=100).until(
                ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
            )

            driver.find_element(By.ID, "rdveriKaynagi_1").click()


            WebDriverWait(driver, timeout=20).until(
            ec.visibility_of_element_located((By.ID, "ddlIller"))
            )   
            il = Select(driver.find_element(By.ID, 'ddlIller'))
            il.select_by_index(ilInd)
            il_name = il.first_selected_option.text
            time.sleep(1)

            WebDriverWait(driver, timeout=20).until(
            ec.visibility_of_element_located((By.ID, "ddlIlceler"))
            )   
            ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
            ilce.select_by_index(ilceInd)
            ilce_name = ilce.first_selected_option.text
            time.sleep(1)


            WebDriverWait(driver, timeout=20).until(
            ec.visibility_of_element_located((By.ID, "ddlSandiklar"))
            )
            sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
            sandik.select_by_index(str(sandikInd))
            sandik_no = sandik.first_selected_option.text
            
            driver.find_element(By.ID, "btnSorgula").click()
            time.sleep(1)

            WebDriverWait(driver, timeout=20).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )



            KS = driver.find_element(By.ID, "tbMvKayitliSecmenSayisi").get_attribute('value')
            OKKS = driver.find_element(By.ID, "tbMvOyKullananKayitliSecmenSayisi").get_attribute('value')
            KGOK = driver.find_element(By.ID, "tbMvKanunGeregiOyKullananSayisi").get_attribute('value')
            KTO = driver.find_element(By.ID, "tbMvKullanilanToplamOy").get_attribute('value')
            IGO = driver.find_element(By.ID, "tbMvItirazsizGecerliOySayisi").get_attribute('value')
            itirazliGO = driver.find_element(By.ID, "tbMvItirazliGecerliOySayisi").get_attribute('value')
            gecerliOy = driver.find_element(By.ID, "tbMvGecerliOySayisi").get_attribute('value')
            gecersizOy = driver.find_element(By.ID, "tbMvGecersizOySayisi").get_attribute('value')

            CHP =  driver.find_element(By.ID, "txtCHP").get_attribute('value')
            AKP = driver.find_element(By.ID, "txtAkp").get_attribute('value') 
            IYI = driver.find_element(By.ID, "txtIyi").get_attribute('value') 
            YSP = driver.find_element(By.ID, "txtYesilSol").get_attribute('value') 
            MHP = driver.find_element(By.ID, "txtMhp").get_attribute('value') 

            print(CHP,AKP,IYI,YSP,MHP)

            WebDriverWait(driver, timeout=20).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )
            driver.find_element(By.ID, "btnCb").click()

            c_KS = driver.find_element(By.ID, "txtCbKayitliSecmen").get_attribute('value')
            c_OKKS = driver.find_element(By.ID, "txtCbOyKullanan").get_attribute('value')
            c_KGOK = driver.find_element(By.ID, "txtCbKanunGeregi").get_attribute('value')
            c_KTO = driver.find_element(By.ID, "txtCbKullanilanToplamOy").get_attribute('value')
            c_IGO = driver.find_element(By.ID, "txtCbItirazsizligecerli").get_attribute('value')
            c_itirazliGO = driver.find_element(By.ID, "txtCbItirazligecerli").get_attribute('value')
            c_gecerliOy = driver.find_element(By.ID, "txtCbGecerliOy").get_attribute('value')
            c_gecersizOy = driver.find_element(By.ID, "txtCbGercersizOy").get_attribute('value')


            RTE = driver.find_element(By.ID, "txtCB1").get_attribute('value')
            MI = driver.find_element(By.ID, "txtCB2").get_attribute('value')
            KK = driver.find_element(By.ID, "txtCB3").get_attribute('value')
            SO = driver.find_element(By.ID, "txtCB4").get_attribute('value')

            print(RTE,MI,KK,SO)
            print(il_name,ilce_name,sandik_no)
