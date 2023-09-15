from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver

SIMILAR_ACCOUNT = "pubity"
USERNAME = "your username"
PASSWORD = "your password"


class InstaFollower:

    def __init__(self):
        self.aano_div = None
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(10)
        username_input_box = self.driver.find_element(By.NAME, "username")
        username_input_box.send_keys(USERNAME)
        password_input_box = self.driver.find_element(By.NAME, "password")
        password_input_box.send_keys(PASSWORD)
        password_input_box.send_keys(Keys.ENTER)
        sleep(10)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        sleep(5)
        self.aano_div = self.driver.find_element(by=By.CLASS_NAME, value="_aano")
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollIntoView();", self.aano_div)
            sleep(3)

    def follow(self):
        buttons = self.aano_div.find_elements(By.TAG_NAME, "button")
        for _ in buttons:
            if _.text == "Follow":
                _.click()
                sleep(10)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
