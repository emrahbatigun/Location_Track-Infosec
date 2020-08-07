import pygeoip
import requests
import sys
import webbrowser
from selenium import webdriver
import time


ip_addr = input("Target IP : ")
geoip = pygeoip.GeoIP('GeoliteCity.dat')
res = geoip.record_by_addr(ip_addr)

for key, val in res.items():
    print(f'{key} : {val}')

location = str(res['latitude']) + ' '+ str(res['longitude'])
base_url ='https://www.google.com/maps/place/'
last_url = base_url + location

driver = webdriver.Chrome(r'C:\Users\Emrah\Desktop\PythonProjects\chromedriver.exe')
driver.get(last_url)
driver.maximize_window()
time.sleep(2)

tarif_button = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[5]/div[1]/div/button')
tarif_button.click()

my_ip = requests.get('https://api.ipify.org').text
res = geoip.record_by_addr(my_ip)

my_loc = str(res['latitude']) + ' ' + str(res['longitude'])
driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(my_loc)
search_button = driver.find_element_by_xpath('//*[@id="directions-searchbox-0"]/button[1]')
search_button.click()


while True:
    pass