from django.contrib.auth.hashers import make_password
from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.system.models import *


class PermissionGroupSerializer(BaseSerializer):

    class PermissionItemSerializer(BaseSerializer):

        class Meta:
            model = Permission
            fields = ['id', 'name', 'code']
            ref_name = 'apps.system.PermissionGroupSerializer.PermissionItemSerializer'

    permission_items = PermissionItemSerializer(source='permission_set', many=True, label='权限')

    class Meta:
        model = PermissionGroup
        fields = ['id', 'name', 'permission_items']


class RoleSerializer(BaseSerializer):

    class PermissionItemSerializer(BaseSerializer):

        class Meta:
            model = Permission
            fields = ['id', 'name', 'code']
            ref_name = 'apps.system.RoleSerializer.PermissionItemSerializer'

    permission_items = PermissionItemSerializer(source='permission_set', many=True, read_only=True, label='权限Items')

    class Meta:
        model = Role
        read_only_fields = ['id', 'permission_items', 'update_time', 'create_time']
        fields = ['name', 'code', 'remark', 'permission_set', *read_only_fields]
        validators = [TeamUniqueValidator(fields=['name'], message='名称已存在')]


class UserSerializer(BaseSerializer):

    class RoleItemSerializer(BaseSerializer):

        class Meta:
            model = Role
            fields = ['id', 'name', 'permission_set']
            ref_name = 'apps.system.UserSerializer.RoleItemSerializer'

    role_items = RoleItemSerializer(source='role_set', many=True, read_only=True, label='角色Items')

    class Meta:
        model = User
        read_only_fields = ['id', 'role_items', 'permissions', 'is_manager', 'update_time', 'create_time']
        fields = ['username', 'name', 'code', 'phone', 'role_set',  'remark',
                  'is_active', *read_only_fields]
        validators = [TeamUniqueValidator(fields=['username'], message='用户名已存在/已删除'),
                      TeamUniqueValidator(fields=['name'], message='名称已存在/已删除')]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['username'])
        return super().create(validated_data)

    def save(self, **kwargs):
        permissions = []
        if role_set := self.validated_data.get('role_set'):
            permissions = {permission.code for role in role_set.prefetch_related('permission_set').all()
                           for permission in role.permission_set.all()}

        kwargs['permissions'] = list(permissions)
        return super().save(**kwargs)


__all__ = [
    'PermissionGroupSerializer', 'RoleSerializer', 'UserSerializer',
]
