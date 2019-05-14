from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

d = input("Link to Boolean search profile")

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome('/Users/hnguyen/chromedriver',chrome_options=options)
driver.get(d)

SCROLL_PAUSE_TIME = 0.5


pag.click(919,256)
print("Connect")
time.sleep(2)
pag.click(880,611)
print("Sent")
time.sleep(2)
pag.typewrite("Hello, please add me on LinkedIn")
pag.click(927,636)
