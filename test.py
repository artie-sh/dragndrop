import driver
from selenium.webdriver.common.by import By

class Test:

    d = None
    ac = None
    base_url = 'http://jqueryui.com/droppable/'
    draggable = "//div[@id='draggable']"
    droppable = "//div[@id='droppable']"

    def __init__(self):
        localdriver = driver.Driver()
        self.d = localdriver.get_driver()
        self.ac = localdriver.get_actionchains()

    def run(self):
        self.d.get(self.base_url)
        self.d.switch_to.frame(frame_reference=self.d.find_element_by_xpath("//iframe[@class='demo-frame']"))
        self.ac.drag_and_drop(self.d.find_element_by_xpath(self.draggable), self.d.find_element_by_xpath(self.droppable)).perform()


test = Test()
test.run()