import time

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # submit edit
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group create
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def edit(self, line, group):
        wd = self.app.wd
        self.open_groups_page()
        # select group
        wd.find_element_by_xpath("//*[@id='content']/form/span[" + str(line) + "]/input").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.open_groups_page()

    def delete(self, line):
        wd = self.app.wd
        self.open_groups_page()
        #if we have only one group, xpath locator must be without []
        if self.count() == 1:
            xpath = "//*[@id='content']/form/span/input"
        else:
            xpath = "//*[@id='content']/form/span[" + str(line) + "]/input"
        wd.find_element_by_xpath(xpath).click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        time.sleep(1)
        return len(wd.find_elements_by_name("selected[]"))