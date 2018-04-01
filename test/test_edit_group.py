from model.group import Group

def test_edit_group_name(app):
    group_param = 0
    group_count = app.group.count()
    if (group_param > 0) and (group_param <= group_count):
        app.group.edit(group_param, Group(name="New group"))
    else:
        app.group.create(Group(name="test"))
        app.group.edit(group_count + 1, Group(name="New group"))

#def test_edit_group_header(app):
 #   app.group.edit(2, Group(header="New header"))