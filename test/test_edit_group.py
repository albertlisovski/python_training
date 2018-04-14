from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group_param = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[group_param].id
    app.group.edit(group_param, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_param] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
#    group_param = 2
#    group_count = app.group.count()
#    if (group_param > group_count) or (group_param < 1):
#        app.group.create(Group(header="test"))
#        group_param = group_count + 1
#    old_groups = app.group.get_group_list()
#    app.group.edit(group_param, Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
