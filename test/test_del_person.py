from model.person import Person
from random import randrange
import pytest

@pytest.mark.repeat(10)
def test_delete_person(app, db, check_ui):
    if len(db.get_person_list()) == 0:
        app.person.create(Person(lname="Zadornov"))

    old_persons = db.get_person_list()

    i = randrange(len(old_persons))
    person = old_persons[i]

    app.person.delete_person_by_id(person.id)

    new_persons = db.get_person_list()
    assert len(old_persons) - 1 == len(new_persons)
    old_persons[i:i+1] = []
    assert old_persons == new_persons
    if check_ui:
        assert sorted(new_persons, key=Person.id_or_max) == sorted(app.person.get_person_list(), key=Person.id_or_max)