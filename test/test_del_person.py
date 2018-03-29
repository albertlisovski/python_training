def test_delete_person(app):
    app.session.login(username="admin", password="secret")
    app.person.delete(1)
    app.session.logout()