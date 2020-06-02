from selenium import webdriver
from time import sleep
from secrets import sw
 

class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sugs = self.driver.find_element_by_xpath('//a[contains(text(), Suggestions)]');
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_element_by_tag_name('a')
        names = [name.text for name in links if name.txt != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]//button")\
            .click()
        return names
    

my_bot = InstaBot('robsonvpires@gmail.com', sw)
