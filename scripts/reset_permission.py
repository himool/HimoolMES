from apps.system.models import Team, PermissionGroup, Permission
import itertools


PERMISSIONS = [
    {
        'name': '基础数据',
        'permissions': [
            {'name': '物料分类查询', 'code': 'material_category.get'},
            {'name': '物料分类创建', 'code': 'material_category.post'},
            {'name': '物料分类编辑', 'code': 'material_category.put'},
            {'name': '物料分类删除', 'code': 'material_category.delete'},
        ],
    },
]


def run(*args):
    PermissionGroup.objects.all().delete()

    for team, permission_group_item in itertools.product(Team.objects.all(), PERMISSIONS):
        permission_group = PermissionGroup.objects.create(name=permission_group_item['name'], team=team)
        Permission.objects.bulk_create([Permission(group=permission_group, name=item['name'], code=item['code'], team=team)
                                        for item in permission_group_item['permissions']])
