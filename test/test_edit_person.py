from model.person import Person
import time

def test_edit_person(app):
    app.person.edit(2, Person(fname="Petr", mname="Petrovich", lname="Petrov", nname="Petya", phone="+78888888888", email="mail@yandex.ru", address=str(time.ctime())))