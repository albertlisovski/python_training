from model.person import Person
import time

def test_edit_person(app):
    person_param = 1
    person_count = app.person.count()
    if (person_param > 0) and (person_param <= person_count):
        app.person.edit(person_param, Person(address=str(time.ctime())))
    else:
        app.person.create(Person(lname="Zadornov"))
        app.person.edit(person_count + 1, Person(address=str(time.ctime())))