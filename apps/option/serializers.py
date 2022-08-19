from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.system.models import *
from apps.material.models import *


# System
class RoleOptionSerializer(BaseSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name', 'permission_set']


# Material
class MaterialCategoryOptionSerializer(BaseSerializer):

    class Meta:
        model = MaterialCategory
        fields = ['id', 'name']


class MaterialOptionSerializer(BaseSerializer):

    class Meta:
        model = Material
        fields = ['id', 'number', 'name', 'spec', 'unit']


__all__ = [
    'RoleOptionSerializer', 'MaterialCategoryOptionSerializer', 'MaterialOptionSerializer',
]
