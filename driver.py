from selenium import webdriver
from selenium.webdriver import ActionChains

class Driver:

    driver = None
    action_chains = None

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.action_chains = ActionChains(self.driver)

    def get_driver(self):
        return self.driver

    def get_actionchains(self):
        return self.action_chains