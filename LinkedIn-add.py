from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

#SCROLL_PAUSE_TIME = 0.5

def convert_boolean(s):
    snew = str(s).replace(' ','%20')
    snew = snew.replace('"','%22')
    snew = snew.replace('&','%26')
    sfull = 'https://www.linkedin.com/search/results/people/?keywords='+snew+'&origin=SWITCH_SEARCH_VERTICAL '
    return(sfull)


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
    pag.typewrite("Hi, please connect with me")
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

def run(b):
    d = convert_boolean(str(b))

    for i in range(1, 21):

        if i == 1:
            d = d[0:-1] + '&page=' + str(i)
        if i in range(1, 11):
            d = d[0:-1] + str(i)
        if i >= 11:
            d = d[0:-2] + str(i)

        options = Options()
        options.add_argument("user-data-dir=/tmp/xxx")
        driver = webdriver.Chrome('/Users/xxx/chromedriver', chrome_options=options)
        driver.get(d)

        time.sleep(3)

        for pos in list(pag.locateAllOnScreen('small_button.png', region=(1754, 400, 260, 1800))):
            cen = pag.center(pos)
            send_note(get_xy(str(cen)))

        driver.quit()

if __name__ == '__main__':
    booleanstring1 = input("String 1:")
    booleanstring2 = input("String 2:")
    booleanstring3 = input("String 3:")
    booleanstring4 = input("String 4:")
    booleanstring5 = input("String 5:")
    run(booleanstring1)
    run(booleanstring2)
    run(booleanstring3)
    run(booleanstring4)
    run(booleanstring5)
