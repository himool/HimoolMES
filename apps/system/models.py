from extensions.common.base import *
from extensions.models import *


class Team(Model):

    number = CharField(max_length=32, unique=True, verbose_name='编号')
    expiry_time = DateTimeField(verbose_name='到期时间')
    update_time = DateTimeField(auto_now=True, verbose_name='修改时间')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')


class PermissionGroup(Model):
    """权限分组"""

    name = CharField(max_length=64, verbose_name='分组名称')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='permission_group_set')

    class Meta:
        unique_together = [('name', 'team')]


class Permission(Model):
    """权限"""

    group = ForeignKey('system.PermissionGroup', on_delete=CASCADE,
                       related_name='permission_set', verbose_name='权限分组')
    name = CharField(max_length=64, verbose_name='权限名称')
    code = CharField(max_length=64, verbose_name='权限代码')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='permission_set')

    class Meta:
        unique_together = [('name', 'team'), ('code', 'team')]


class Role(Model):
    """角色"""

    name = CharField(max_length=64, verbose_name='名称')
    code = CharField(max_length=64, null=True, blank=True, verbose_name='代码')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    permission_set = ManyToManyField('system.Permission', blank=True, related_name='role_set', verbose_name='权限')
    update_time = DateTimeField(auto_now=True, verbose_name='修改时间')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='role_set')

    class Meta:
        unique_together = [('name', 'team')]


class User(RefModel):
    """用户[Reference]"""

    username = CharField(max_length=32, verbose_name='用户名')
    password = CharField(max_length=256, verbose_name='密码')
    name = CharField(max_length=64, verbose_name='名称')
    phone = CharField(max_length=32, null=True, blank=True, verbose_name='手机号')
    role_set = ManyToManyField('system.Role', blank=True, related_name='user_set', verbose_name='角色')
    permissions = JSONField(default=list, verbose_name='权限')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    is_manager = BooleanField(default=False, verbose_name='管理员状态')
    is_active = BooleanField(default=True, verbose_name='激活状态')
    update_time = DateTimeField(auto_now=True, verbose_name='修改时间')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='user_set')

    class Meta:
        unique_together = [('username', 'team'), ('name', 'team')]


__all__ = [
    'Team', 'PermissionGroup', 'Permission', 'Role', 'User',
]
