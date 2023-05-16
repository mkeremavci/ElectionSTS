import time
import json
import os
from tqdm import tqdm, trange


if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)
else:
    data = {'cm': {}, 'mv': {}}
    
with open('data.json', 'w') as f:
    f.write(json.dumps(data, indent=4))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   # Do not wait for full page load

op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op, desired_capabilities=caps)


for ilInd in trange(1, 82, desc="scraping cities"):
    driver.get('https://sts.chp.org.tr')
    
    """
    Toplam Ilce ve Sandik
    """
    ilInd = str(int(ilInd))
    WebDriverWait(driver, timeout=10).until(
        ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
    )
    driver.find_element(By.ID, "rdveriKaynagi_1").click()

    il = Select(driver.find_element(By.ID, 'ddlIller'))
    il.select_by_index(ilInd)
    il_name = driver.find_element(By.ID, 'ddlIller').get_attribute('value')

    print(il_name)

    #####
    if il_name not in data['cm']:
        data['cm'][il_name] = {}
        data['mv'][il_name] = {}
    #####

    tot_ilce = len(list(data['cm'][il_name].keys()))
    
    time.sleep(1)

    ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
    ilceOptions = ilce.options
    toplamIlce = len(ilceOptions)
    ilce.select_by_index('1')
    
    time.sleep(1)

    sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
    sandikOptions = sandik.options
    toplamSandik = len(sandikOptions)

    for ilceInd in trange(1, toplamIlce, desc="scraping a district"):
        if ilceInd <= tot_ilce:
            continue

        for sandikInd in range(1, toplamSandik):
            driver.get('https://sts.chp.org.tr')

            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "rdveriKaynagi_1"))
            )
            driver.find_element(By.ID, "rdveriKaynagi_1").click()
            il = Select(driver.find_element(By.ID, 'ddlIller'))
            il.select_by_index(ilInd)
            il_name = driver.find_element(By.ID, 'ddlIller').get_attribute('value') ###

            print(il_name)

            time.sleep(1)

            ilce = Select(driver.find_element(By.ID, 'ddlIlceler'))
            ilce.select_by_index(ilceInd)
            ilce_name = driver.find_element(By.ID, 'ddlIlceler').get_attribute('value') ###

            #####
            if ilce_name not in data[il_name]:
                data['cm'][il_name][ilce_name] = {}
                data['mv'][il_name][ilce_name] = {}
            #####

            time.sleep(1)

            sandik = Select(driver.find_element(By.ID, 'ddlSandiklar'))
            sandik.select_by_index(str(sandikInd))
            sandik_no = driver.find_element(By.ID, 'ddlSandiklar').get_attribute('value') ###

            #####
            if sandik_no not in data[il_name][ilce_name]:
                data['cm'][il_name][ilce_name][sandik_no] = {}
                data['mv'][il_name][ilce_name][sandik_no] = {}
            #####
            
            driver.find_element(By.ID, "btnSorgula").click()

            time.sleep(1)

            """
            MV
            """
            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )

            OKKS = driver.find_element(By.ID, "tbMvKayitliSecmenSayisi").get_attribute('value')
            KGOK = driver.find_element(By.ID, "tbMvOyKullananKayitliSecmenSayisi").get_attribute('value')
            KTO = driver.find_element(By.ID, "tbMvKullanilanToplamOy").get_attribute('value')
            IGO = driver.find_element(By.ID, "tbMvItirazsizGecerliOySayisi").get_attribute('value')
            itirazliGO = driver.find_element(By.ID, "tbMvItirazliGecerliOySayisi").get_attribute('value')
            gecerliOy = driver.find_element(By.ID, "tbMvGecerliOySayisi").get_attribute('value')
            gecersizOy = driver.find_element(By.ID, "tbMvGecersizOySayisi").get_attribute('value')

            #####
            data['mv'][il_name][ilce_name][sandik_no]['stats'] = {
                'KayitliSecmenSayisi': OKKS,
                'OyKullananKayitliSecmenSayisi': KGOK,
                'KullanilanToplamOy': KTO,
                'ItirazsizGecerliOySayisi': IGO,
                'ItirazliGecerliOySayisi': itirazliGO,
                'GecerliOySayisi': gecerliOy,
                'GecersizOySayisi': gecersizOy,
            }
            #####

            CHP =  driver.find_element(By.ID, "txtCHP").get_attribute('value')
            AKP = driver.find_element(By.ID, "txtAkp").get_attribute('value') 
            IYI = driver.find_element(By.ID, "txtIyi").get_attribute('value') 
            YSP = driver.find_element(By.ID, "txtYesilSol").get_attribute('value') 
            MHP = driver.find_element(By.ID, "txtMhp").get_attribute('value')

            data['mv'][il_name][ilce_name][sandik_no]['adaylar'] = {
                'CHP': CHP,
                'AKP': AKP,
                'İYİP': IYI,
                'YSP': YSP,
                'MHP': MHP,
            }

            """
            CB
            """
            WebDriverWait(driver, timeout=10).until(
                ec.visibility_of_element_located((By.ID, "btnCb"))
            )
            driver.find_element(By.ID, "btnCb").click()

            OKKS = driver.find_element(By.ID, "txtCbKayitliSecmen").get_attribute('value')
            KGOK = driver.find_element(By.ID, "txtCbOyKullanan").get_attribute('value')
            KTO = driver.find_element(By.ID, "txtCbKullanilanToplamOy").get_attribute('value')
            IGO = driver.find_element(By.ID, "txtCbItirazsizligecerli").get_attribute('value')
            itirazliGO = driver.find_element(By.ID, "txtCbItirazligecerli").get_attribute('value')
            gecerliOy = driver.find_element(By.ID, "txtCbGecerliOy").get_attribute('value')
            gecersizOy = driver.find_element(By.ID, "txtCbGercersizOy").get_attribute('value')

            #####
            data['cm'][il_name][ilce_name][sandik_no]['stats'] = {
                'KayitliSecmenSayisi': OKKS,
                'OyKullananKayitliSecmenSayisi': KGOK,
                'KullanilanToplamOy': KTO,
                'ItirazsizGecerliOySayisi': IGO,
                'ItirazliGecerliOySayisi': itirazliGO,
                'GecerliOySayisi': gecerliOy,
                'GecersizOySayisi': gecersizOy,
            }
            #####

            RTE = driver.find_element(By.ID, "txtCB1").get_attribute('value')
            MI = driver.find_element(By.ID, "txtCB2").get_attribute('value')
            KK = driver.find_element(By.ID, "txtCB3").get_attribute('value')
            SO = driver.find_element(By.ID, "txtCB4").get_attribute('value')

            data['cm'][il_name][ilce_name][sandik_no]['adaylar'] = {
                'RECEP TAYYİP ERDOĞAN': RTE,
                'MUHARREM İNCE': MI,
                'KEMAL KILIÇDAROĞLU': KK,
                'SİNAN OĞAN': SO,
            }

        with open('data.json', 'w') as f:
            f.write(json.dumps(data, indent=4))
