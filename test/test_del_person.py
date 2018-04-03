from model.person import Person


def test_delete_person(app):
    person_param = 2
    person_count = app.person.count()
    if (person_param > person_count) or (person_param < 0):
        app.person.create(Person(lname="Zadornov"))
        person_param = person_count + 1
    old_persons = app.person.get_person_list()
    app.person.delete(person_param)
    new_persons = app.person.get_person_list()
    assert len(old_persons) - 1 == len(new_persons)
    old_persons[person_param - 1:person_param] = []
    assert old_persons == new_persons