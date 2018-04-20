# -*- coding: utf-8 -*-
from model.person import Person
import time
import pytest
import random ,string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_email():
    symbols = string.ascii_letters + string.digits
    username = "".join(random.choice(symbols) for i in range(random.randrange(8)))
    domainname = "".join(random.choice(symbols) for i in range(random.randrange(8)))
    return username + "@" + domainname + ".ru"


testdata = [
    Person(fname="", mname="", lname="")] + [
    Person(fname=random_string("fname", 10), mname=random_string("mname", 20), lname=random_string("lname", 20), email=random_email(),
           email2=random_email(), email3=random_email())
    for i in range(5)
]


@pytest.mark.parametrize("person", testdata, ids=[repr(x) for x in testdata])
def test_add_person(app, person):
    old_persons = app.person.get_person_list()
    app.person.create(person)
    new_persons = app.person.get_person_list()
    assert len(old_persons) + 1 == len(new_persons)
    old_persons.append(person)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)


