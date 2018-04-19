import time, re
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
        self.change_field_value("home", person.homephone)
        self.change_field_value("mobile", person.mobilephone)
        self.change_field_value("work", person.workphone)
        self.change_field_value("secondary", person.secondaryphone)
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

    def edit(self, index, person):
        wd = self.app.wd
        # select item
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(index + 2) +"]/td[8]/a/img").click()
        self.fill_person_form(wd, person)
        # submit person update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.person_cache = None
        time.sleep(1)

    def delete(self, index):
        wd = self.app.wd
        #select 1st item
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[1]").click()
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                for i in range(4):
                    if i >= len(all_phones):
                        all_phones.append("")
                self.person_cache.append(
                    Person(fname=firstname, lname=lastname, id=id, homephone=all_phones[0], mobilephone=all_phones[1],
                           workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.person_cache)

    def open_person_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        time.sleep(1)

    def open_person_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()
        time.sleep(1)

    def get_person_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_person_to_edit_by_index(index)
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Person(fname=firstname, lname=lastname, id=id, homephone=homephone, workphone=workphone,
                      mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_person_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_person_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Person(homephone=homephone, workphone=workphone,
                      mobilephone=mobilephone, secondaryphone=secondaryphone)