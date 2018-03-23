# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from person import Person

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_person(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_person(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_person(wd, Person(fname="Ivan", mname="Ivanovich", lname="Ivanov", nname="Vanya", phone="+79999999999", email="mail@mail.ru"))
        # wd.find_element_by_name("theform").click()
        self.logout(wd)

    def test_add_empty_person(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_person(wd, Person(fname="", mname="", lname="", nname="", phone="", email=""))
        # wd.find_element_by_name("theform").click()
        self.logout(wd)

    def logout(self, wd):
       wd.find_element_by_link_text("Logout").click()

    def create_person(self, wd, person):
        # add new person
        wd.find_element_by_link_text("add new").click()
        # fill person form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(person.fname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(person.mname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(person.lname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(person.nname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(person.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(person.email)
        # submit person creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        # login
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
