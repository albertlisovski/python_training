# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from person import Person
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_person(app):
    app.login(username="admin", password="secret")
    app.create_person(Person(fname="Ivan", mname="Ivanovich", lname="Ivanov", nname="Vanya", phone="+79999999999", email="mail@mail.ru"))
    app.logout()

def test_add_empty_person(app):
    app.login(username="admin", password="secret")
    app.create_person(Person(fname="", mname="", lname="", nname="", phone="", email=""))
    app.logout()

