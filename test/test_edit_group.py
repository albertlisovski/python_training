from model.group import Group

def test_edit_group_name(app):
    app.group.edit(1, Group(name="New group"))

def test_edit_group_header(app):
    app.group.edit(2, Group(header="New header"))