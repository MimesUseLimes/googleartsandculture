import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
# import undetected_chromedriver as uc
# from selenium_stealth import stealth
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC

## selenium stealth
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)
# driver = webdriver.Chrome(options=options)

## undetected chromedriver
# driver = uc.Chrome()
# options = uc.Options()
# options.add_argument('192.168.4.97:17432')
# browser = uc.Chrome(options=options)
# options.add_argument(r'--user-data-dir=C:\Users\shane\AppData\Local\Google\Chrome\User Data\Default')
# stealth(driver,languages=["en-US","en"],vendor="Google Inc.",platform="Win32",webgl_vendor = "Intel Inc.",renderer="Intel Irs OpenGL Engine")

def main():

    chrome_driver_path = r"C:\Users\shane\Documents\googleartsandculture\chromedriver.exe" 

    ## random agent to bypass bot detector
    options = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    # print(user_agent)
    options.add_argument(f'--user-agent={user_agent}')

    # disable infobar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # set driver
    cService = webdriver.ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(options=options, service = cService)

    # open browser
    driver.get("https://artsandculture.google.com")
    driver.maximize_window()
    driver.fullscreen_window()

    # Click on Menu
    driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[2]/div[1]/div[1]/div[1]').click()
    time.sleep(0.5)
    # Click on Category
    category = '//*[@id="yDmH0d"]/div[1]/div[3]/nav/ul[2]/li[1]/a' # EDITABLE
    driver.find_element(By.XPATH,category).click() 
    time.sleep(2)
    # Click Type of Collection
    collection = '//*[@id="tab_pop"]/div/div/div[1]/a/span/div[2]/h3' # EDITABLE
    driver.find_element(By.XPATH,collection).click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="exp_tab_popular"]/div/div/div[3]/span/div[1]/div[3]/a').click()
    # driver.find_element(By.XPATH,'//*[@id="exp_tab_popular"]/div/div/div[3]/span/div[29]/div[5]/a').click() # this is the picture at the end of the collection but not detectable b/c images dynamically load as you scroll thru

    viewing_time = 7 #EDITABLE
    scroll_direction = Keys.RIGHT
    # continuously scroll thru
    while True:      
        initial_url = driver.current_url # Get the initial URL before sending keys
        time.sleep(viewing_time)
        ActionChains(driver).send_keys(scroll_direction).perform()
        # time.sleep(0.5)
        if driver.current_url == initial_url:
            if scroll_direction == Keys.RIGHT:
                scroll_direction = Keys.LEFT
            else:
                scroll_direction = Keys.RIGHT

if __name__ == "__main__":
    main()