from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.system.models import *


# System
class RoleOptionSerializer(BaseSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name', 'permission_set']


__all__ = [
    'RoleOptionSerializer',
]
