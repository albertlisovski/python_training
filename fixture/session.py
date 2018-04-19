
from selenium.common.exceptions import NoSuchElementException
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        try:
            wd.find_element_by_link_text("Logout")
        except NoSuchElementException:
            return False
        return True

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='top']/form/b").text[1:-1]

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.get_logged_user() == username:
                return
            else:
                self.logout()
        self.login(username,password)

