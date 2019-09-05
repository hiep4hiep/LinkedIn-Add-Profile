from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

#SCROLL_PAUSE_TIME = 0.5

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
    pag.click(867,247)
    pag.typewrite("Hi, I am Thanh from Deloitte, I'd like to connect with you for future opportunity from us. If you are interested please kindly share with me your email/contact info for further discussion. BRs, thanhtle@deloitte.com")
    pag.click(927,305)
    pag.click(90,252)
    time.sleep(2)

def get_xy(box):
    x = box[8:box.find(', y')]
    y = box[box.find('y=')+2:-1]
    l  = [x,y]
    return(l)

def connect():
    find_button_and_click('my_button.png')
    send_note()

def run():
    d = input("Search link:")

    for i in range(1, 25):

        if i == 1:
            d = d[0:-1] + '&page=' + str(i)
        if i in range(1, 11):
            d = d[0:-1] + str(i)
            print(i)
        if i >= 11:
            d = d[0:-2] + str(i)
            print(i)

        # d = input("Link to Boolean search profile: ")
        # n = str(input("Note to candidate: "))

        options = Options()
        options.add_argument("user-data-dir=/tmp/thanh")
        driver = webdriver.Chrome('/Users/hnguyen/chromedriver', chrome_options=options)
        driver.get(d)

        time.sleep(3)
        # take_screenshot()

        for pos in list(pag.locateAllOnScreen('small_button.png', region=(1754, 400, 260, 1800))):
            cen = pag.center(pos)
            send_note(get_xy(str(cen)))

        driver.quit()

if __name__ == '__main__':
    run()
