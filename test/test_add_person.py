# -*- coding: utf-8 -*-
from model.person import Person
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_person(app):
    app.session.login(username="admin", password="secret")
    app.person.create(Person(fname="Ivan", mname="Ivanovich", lname="Ivanov", nname="Vanya", phone="+79999999999", email="mail@mail.ru"))
    app.session.logout()

def test_add_empty_person(app):
    app.session.login(username="admin", password="secret")
    app.person.create(Person(fname="", mname="", lname="", nname="", phone="", email=""))
    app.session.logout()

