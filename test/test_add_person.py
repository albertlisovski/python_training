# -*- coding: utf-8 -*-
from model.person import Person
import time

def test_add_person(app):
    old_persons = app.person.get_person_list()
    person = Person(fname="Ivan", mname="Ivanovich", lname="Ivanov", nname="Vanya", phone="+79999999999", email="mail@mail.ru", address=str(time.ctime()))
    app.person.create(person)
    new_persons = app.person.get_person_list()
    assert len(old_persons) + 1 == len(new_persons)
    old_persons.append(person)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)

#def test_add_empty_person(app):
#    app.person.create(Person(fname="", mname="", lname="", nname="", phone="", email=""))

