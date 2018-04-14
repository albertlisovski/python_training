import time
from model.person import Person

class PersonHelper:
    def __init__(self, app):
        self.app = app

    def fill_person_form(self, wd, person):
        # fill person form
        self.change_field_value("firstname", person.fname)
        self.change_field_value("middlename", person.mname)
        self.change_field_value("lastname", person.lname)
        self.change_field_value("nickname", person.nname)
        self.change_field_value("home", person.phone)
        self.change_field_value("email", person.email)
        self.change_field_value("address", person.address)

    def change_field_value(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(text)

    def create(self, person):
        # add new person
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_person_form(wd, person)
        # submit person creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        self.person_cache = None

    def edit(self, line, person):
        wd = self.app.wd
        # select item
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(line+1) +"]/td[8]/a/img").click()
        self.fill_person_form(wd, person)
        # submit person update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.person_cache = None

    def delete(self, line):
        wd = self.app.wd
        #select 1st item
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(line + 1) + "]/td[1]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.person_cache = None
        time.sleep(1)

    def count(self):
        wd = self.app.wd
        time.sleep(1)
        return len(wd.find_elements_by_name("selected[]"))

    person_cache = None

    def get_person_list(self):
        if self.person_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            time.sleep(1)
            #self.open_groups_page()
            self.person_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.person_cache.append(Person(lname=text, id=id))
        return list(self.person_cache)

