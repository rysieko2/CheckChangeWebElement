import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# --------------------------
# 1 = Linux  | 2 = Windows

system = 2
# -------------------------

if system == 1:
    geckoDriverPath = "/home/krzys/geckodriver"
else:
    geckoDriverPath = "E:/geckodriver"


options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.set_preference('permissions.default.stylesheet', 2)
options.set_preference('permissions.default.image', 2)
options.set_preference('javascript.enabled', False)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

firstXpath = "//div//a[contains(@href,'http')]"
boxXpath = '//*[@class="container vspace"]'
oNomXpath = '//*[@align="center"]'
oTreXpath = "//div//p"

# 1 = Linux
# 2 = Windows




class Driver(object):
    def __init__(self):
        driver = webdriver.Firefox(executable_path=geckoDriverPath, options=options)
        # wait = WebDriverWait(driver, 10)
        driver.get("http://www.tbs-wroclaw.com.pl/mieszkania-na-wynajem/")
        time.sleep(2)
        self.driver = driver

    def first(self):
        firstElement = self.driver.find_element_by_xpath(firstXpath)
        first = firstElement.text
        return first

    def first_click(self):
        firstElement = self.driver.find_element_by_xpath(firstXpath)
        firstElement.click()

    def new_loc_link(self):
        firstElement = self.driver.find_element_by_xpath(firstXpath)
        firstElement.click()
        locLink = self.driver.current_url
        return locLink

    def box(self):
        boxElement = self.driver.find_element_by_xpath(boxXpath)
        box = boxElement.text
        return box

    def ad_number(self):
        adEle = self.driver.find_element_by_xpath(oNomXpath)
        add = adEle.text
        return add

    def ad_contents(self):
        infoEle = self.driver.find_element_by_xpath(oTreXpath)
        content = infoEle.text
        return content

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()
