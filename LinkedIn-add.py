from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time


#SCROLL_PAUSE_TIME = 0.5
def find_button_all(button):
    pos = list(pag.locateAllOnScreen(button, region=(1,2,3,4)))

def find_button_and_click(button):
    buttonx, buttony = pag.locateCenterOnScreen(button, region=(2700,800,700,700))
    print(buttonx//2)
    print(buttony//2)
    pag.click(buttonx//2, buttony//2)

def take_screenshot():
    im1 = pag.screenshot()
    im1.save('screenshot.png')

def send_note(position):
    print(position[0],position[1])
    pag.click(int(position[0])//2,int(position[1])//2)
    pag.click(906,354)
    pag.typewrite("Hello please connect with me")
    pag.click(1015,450)
    time.sleep(3)

def get_xy(box):
    x = box[8:box.find(', y')]
    y = box[box.find('y=')+2:-1]
    l  = [x,y]
    return(l)

def connect():
    find_button_and_click('my_button.png')
    send_note()

d = 'https://www.linkedin.com/search/results/people/?keywords=CCIE&origin=SWITCH_SEARCH_VERTICAL'

for i in range (1,20):

    #d = input("Link to Boolean search profile: ")
    #n = str(input("Note to candidate: "))

    options = Options()
    options.add_argument("user-data-dir=/tmp/python")
    driver = webdriver.Chrome('/Users/hnguyen/chromedriver',chrome_options=options)
    driver.get(d)

    time.sleep(3)
    #take_screenshot()


    for pos in list(pag.locateAllOnScreen('my_button_small.png', region=(1844,400,268,1584))):
        cen = pag.center(pos)
        send_note(get_xy(str(cen)))

    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(3)

    for pos2 in list(pag.locateAllOnScreen('my_button_small.png', region=(1844,400,268,1584))):
        cen = pag.center(pos2)
        send_note(get_xy(str(cen)))

    if i == 1:
        d = d + '&page='+str(i)
    if i != 1:
        d = d[0:-1] + str(i)

    driver.quit()
