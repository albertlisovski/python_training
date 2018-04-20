import re
from random import randrange

def test_phones_on_home_page(app):
    persons = app.person.get_person_list()
    index = randrange(len(persons))
    person_from_home_page = persons[index]
    person_from_edit_page = app.person.get_person_info_from_edit_page(index)
    assert person_from_home_page.fname == person_from_edit_page.fname
    assert person_from_home_page.lname == person_from_edit_page.lname
    assert person_from_home_page.address == person_from_edit_page.address
    assert person_from_home_page.allphones_from_home_page == merge_phones_like_on_home_page(person_from_edit_page)
    assert person_from_home_page.allemails_from_home_page == merge_emails_like_on_home_page(person_from_edit_page)

def test_phones_on_person_view_page(app):
    person_from_view_page = app.person.get_person_info_from_view_page(0)
    person_from_edit_page = app.person.get_person_info_from_edit_page(0)
    assert person_from_view_page.homephone == person_from_edit_page.homephone
    assert person_from_view_page.workphone == person_from_edit_page.workphone
    assert person_from_view_page.mobilephone == person_from_edit_page.mobilephone
    assert person_from_view_page.secondaryphone == person_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(person):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                   [person.homephone, person.mobilephone, person.workphone, person.secondaryphone]))))

def merge_emails_like_on_home_page(person):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                   [person.email, person.email2, person.email3]))))