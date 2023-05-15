from time import sleep
import pandas as pd
import json

df = pd.read_excel("il_ilce_list.xlsx")

cities = list(df["İL ADI"].unique())
districts = {}
for city in cities:
    districts[city] = list(df.loc[df["İL ADI"] == city]["İLÇE  ADI"].unique())

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

op = webdriver.ChromeOptions()
op.add_argument('headless')

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://sts.chp.org.tr/")

driver.find_element("id", "rdveriKaynagi_1").click();

select = Select(driver.find_element("id", "ddlIller"))
select.select_by_visible_text(cities[0]);

sleep(1)

select = Select(driver.find_element("id", "ddlIlceler"))
select.select_by_visible_text(districts[cities[0]][0]);

sleep(1)

select = Select(driver.find_element("id", "ddlSandiklar"))
options = [opt.text for opt in select.options][1:]
select.select_by_visible_text(options[0]);

driver.find_element("id", "btnSorgula").click();

sleep(20)

