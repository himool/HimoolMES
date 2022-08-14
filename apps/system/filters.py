from extensions.filters import *
from apps.system.models import *


class UserFilter(FilterSet):
    role = NumberFilter(field_name='role_set', label='角色')

    class Meta:
        model = User
        fields = ['role', 'is_active']


__all__ = [
    'UserFilter',
]
