import driver
import pyautogui

class Test:

    d = None
    ac = None
    wait = None

    base_url = 'https://10.131.177.22/the-one/#/login'
    email_input = "//label[text()='Email']/..//input"
    password_input = "//label[text()='Password']/..//input"
    login_button = "//button[text()='Log in']"

    email = ""
    password = ""

    side_element = "//div[contains(@class, 'draggable')]//span[text()='0Apps scenario by sdemian']"
    drop_area = "//div[contains(@class, 'drop-area')]"

    def __init__(self):
        localdriver = driver.Driver()
        self.d = localdriver.get_driver()
        self.wait = localdriver.get_wait()
        self.ac = localdriver.get_actionchains()

    def run(self):
        self.d.get(self.base_url)
        self.d.find_element_by_xpath(self.email_input).send_keys(self.email)
        self.d.find_element_by_xpath(self.password_input).send_keys(self.password)
        self.d.find_element_by_xpath(self.login_button).click()

        #>>> wazne!
        x = self.d.find_element_by_xpath(self.drop_area).location["x"] + self.d.find_element_by_xpath(self.drop_area).size["width"]/2
        y = self.d.find_element_by_xpath(self.drop_area).location["y"] + self.d.find_element_by_xpath(self.drop_area).size["height"]
        pyautogui.moveTo(x, y)
        #<<<

        self.ac.drag_and_drop(self.d.find_element_by_xpath(self.side_element), self.d.find_element_by_xpath(self.drop_area)).perform()

    def quit(self):
        self.d.quit()


test = Test()
test.run()
#test.quit()