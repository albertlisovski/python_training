from model.person import Person

def test_delete_person(app):
    person_param = 2
    person_count = app.person.count()
    if (person_param > 0) and (person_param <= person_count):
        app.person.delete(person_param)
    else:
        app.person.create(Person(lname="Zadornov"))
        app.person.delete(person_count + 1)