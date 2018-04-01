from model.group import  Group

def test_delete_group(app):
    group_param = 1
    group_count = app.group.count()
    if (group_param > 0) and (group_param <= group_count):
        app.group.delete(group_param)
    else:
        app.group.create(Group(name="test"))
        app.group.delete(group_count + 1)