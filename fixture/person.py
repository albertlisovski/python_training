class PersonHelper:
    def __init__(self, app):
        self.app = app

    def create(self, person):
        # add new person
        wd = self.app.wd
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

    def delete_first_person(self):
        wd = self.app.wd
        #select 1st item
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        alert = wd.switch_to_alert()
        alert.accept()