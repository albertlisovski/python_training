class PersonHelper:
    def __init__(self, app):
        self.app = app

    def fill_person_form(self, wd, person):
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
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(person.address)

    def create(self, person):
        # add new person
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_person_form(wd, person)
        # submit person creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit(self, line, person):
        wd = self.app.wd
        # select item
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(line+1) +"]/td[8]/a/img").click()
        self.fill_person_form(wd, person)
        # submit person update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()

    def delete(self, line):
        wd = self.app.wd
        #select 1st item
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(line + 1) + "]/td[1]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

