from model.person import Person
from random import randrange

def test_edit_person(app):
    if app.person.count() == 0:
        app.person.create(Person(lname="Zadornov"))
    old_persons = app.person.get_person_list()
    person_param = randrange(len(old_persons))
    person = Person(lname="New person")
    person.id = old_persons[person_param].id
    app.person.edit(person_param, person)
    new_persons = app.person.get_person_list()
    assert len(old_persons) == len(new_persons)
    old_persons[person_param] = person
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)