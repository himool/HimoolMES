from apps.system.models import Team, PermissionGroup, Permission
import itertools


PERMISSIONS = [

]


def run(*args):
    PermissionGroup.objects.all().delete()

    for team, permission_group_item in itertools.product(Team.objects.all(), PERMISSIONS):
        permission_group = PermissionGroup.objects.create(name=permission_group_item['name'], team=team)
        Permission.objects.bulk_create([Permission(group=permission_group, name=item['name'], code=item['code'], team=team)
                                        for item in permission_group_item['permissions']])
