from model.person import Person
from random import randrange

def test_delete_person(app):
    if app.person.count() == 0:
        app.person.create(Person(lname="Zadornov"))
    old_persons = app.person.get_person_list()
    person_param = randrange(len(old_persons))
    app.person.delete(person_param)
    new_persons = app.person.get_person_list()
    assert len(old_persons) - 1 == len(new_persons)
    old_persons[person_param:person_param+1] = []
    assert old_persons == new_persons