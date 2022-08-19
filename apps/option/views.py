from extensions.common.schema import *
from extensions.common.base import *
from extensions.permissions import *
from extensions.exceptions import *
from extensions.viewsets import *
from apps.option.serializers import *
from apps.option.permissions import *
from apps.option.filters import *
from apps.option.schemas import *
from apps.option.models import *
from apps.system.models import *
from apps.material.models import *


# System
class RoleOptionViewSet(ListViewSet):
    serializer_class = RoleOptionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    prefetch_related_fields = ['permission_set']
    queryset = Role.objects.all()


# Material
class MaterialCategoryOptionViewSet(ListViewSet):
    serializer_class = MaterialCategoryOptionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    queryset = MaterialCategory.objects.all()


class MaterialOptionViewSet(PagingViewSet):
    serializer_class = MaterialOptionSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['type', 'category']
    search_fields = ['number', 'name']
    queryset = Material.objects.all()


__all__ = [
    'RoleOptionViewSet', 'MaterialCategoryOptionViewSet', 'MaterialOptionViewSet',
]
