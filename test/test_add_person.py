# -*- coding: utf-8 -*-
from model.person import Person

def test_add_person(app, db, json_persons, check_ui):
    person = json_persons
    old_persons = db.get_person_list()
    app.person.create(person)
    new_persons = db.get_person_list()
    assert len(old_persons) + 1 == len(new_persons)
    old_persons.append(person)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
    if check_ui:
        assert sorted(new_persons, key=Person.id_or_max) == sorted(app.person.get_person_list(), key=Person.id_or_max)


