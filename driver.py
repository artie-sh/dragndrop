from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:

    driver = None
    action_chains = None
    wait = None

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(60)
        self.action_chains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def get_driver(self):
        return self.driver

    def get_actionchains(self):
        return self.action_chains

    def get_wait(self):
        return self.wait