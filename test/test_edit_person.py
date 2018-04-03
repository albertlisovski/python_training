from model.person import Person

def test_edit_person(app):
    person_param = 1
    person_count = app.person.count()
    if (person_param > person_count) or (person_param < 1):
        app.person.create(Person(lname="Zadornov"))
        person_param = person_count + 1
    old_persons = app.person.get_person_list()
    person = Person(lname="New person")
    person.id = old_persons[person_param - 1].id
    app.person.edit(person_param, person)
    new_persons = app.person.get_person_list()
    assert len(old_persons) == len(new_persons)
    old_persons[person_param - 1] = person
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)