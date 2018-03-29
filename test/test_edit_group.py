from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(1, Group(name="new", header="new", footer="new"))
    app.session.logout()