from model.group import Group
from random import randrange


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group_param = randrange(len(old_groups))
    app.group.delete(group_param)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[group_param:group_param+1] = []
    assert old_groups == new_groups


#def test_delete_group(app):
#    group_param = 1
#    group_count = app.group.count()
#    if (group_param > group_count) or (group_param < 1):
#        app.group.create(Group(name="test"))
#        group_param = group_count + 1
#    old_groups = app.group.get_group_list()
#    app.group.delete(group_param)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
#    old_groups[group_param-1:group_param] = []
#    assert old_groups == new_groups
