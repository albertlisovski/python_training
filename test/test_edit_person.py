from model.person import Person
import time

def test_edit_person(app):
    app.session.login(username="admin", password="secret")
    app.person.edit(2, Person(fname="Petr", mname="Petrovich", lname="Petrov", nname="Petya", phone="+78888888888", email="mail@yandex.ru", address=str(time.ctime())))
    app.session.logout()