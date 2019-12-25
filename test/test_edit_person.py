from model.person import Person
from random import randrange
import pytest

@pytest.mark.repeat(10)
def test_edit_person(app, db, check_ui):
    if len(db.get_person_list()) == 0:
        app.person.create(Person(lname="Zadornov"))

    old_persons = db.get_person_list()

    i = randrange(len(old_persons))
    op = old_persons[i]
    person = Person(fname="Ivan", mname=op.mname, lname="Ivanov", nname=op.nname, homephone=op.homephone,
                    mobilephone=op.mobilephone, workphone=op.workphone, secondaryphone=op.secondaryphone,
                    allphones_from_home_page=op.allphones_from_home_page, email=op.email, email2=op.email2, email3=op.email3,
                    allemails_from_home_page=op.allemails_from_home_page, address=op.address, id=op.id)
    app.person.edit_person_by_id(person)

    new_persons = db.get_person_list()
    assert len(old_persons) == len(new_persons)
    old_persons[i] = person
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)
    if check_ui:
        assert sorted(new_persons, key=Person.id_or_max) == sorted(app.person.get_person_list(), key=Person.id_or_max)