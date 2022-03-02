#!/usr/bin/env python
from selenium import webdriver
import time

url = "https://sede.administracionespublicas.gob.es/icpplustieb/index"
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

driver.find_element_by_xpath("//select[@name='form']/option[text()='Barcelona']").click()
driver.find_element_by_id("btnAceptar").click()
driver.find_element_by_xpath("//select[@name='sede']/option[text()='CNP COMISARIA BADALONA, AVDA. DELS VENTS, 9']").click()
time.sleep(1)
driver.find_element_by_xpath("//select[@name='tramiteGrupo[0]']/option[text()='POLICIA-CERTIFICADOS Y ASIGNACION NIE (NO COMUNITARIOS)']").click()
driver.find_element_by_id("btnAceptar").click()
time.sleep(1)
driver.find_element_by_id("cookie_action_close_header").click()
time.sleep(1)
driver.find_element_by_id("btnEntrar").click()
driver.find_element_by_css_selector("input[type='radio'][value='PASAPORTE']").click()
inputElement = driver.find_element_by_id("txtIdCitado")
inputElement.send_keys('15848')
inputElement = driver.find_element_by_id("txtDesCitado")
inputElement.send_keys('emanuel sanchez')
driver.find_element_by_id("btnEnviar").click()
driver.find_element_by_id("btnEnviar").click()
text = driver.find_element_by_class_name('mf-msg__info').text
print (text)
