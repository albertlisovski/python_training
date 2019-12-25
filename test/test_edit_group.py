from model.group import Group
from random import randrange


def test_edit_group_name(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    i = randrange(len(old_groups))
    group = old_groups[i]
    group.name = "New group"
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[i] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)