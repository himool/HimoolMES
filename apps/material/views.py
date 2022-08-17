from extensions.common.schema import *
from extensions.common.base import *
from extensions.permissions import *
from extensions.exceptions import *
from extensions.viewsets import *
from apps.material.serializers import *
from apps.material.permissions import *
from apps.material.filters import *
from apps.material.schemas import *
from apps.material.models import *


class MaterialCategoryViewSet(ModelViewSet):
    """物料分类"""

    serializer_class = MaterialCategorySerializer
    permission_classes = [IsAuthenticated, MaterialCategoryPermission]
    search_fields = ['name', 'remark']
    ordering_fields = ['id', 'name']
    queryset = MaterialCategory.objects.all()


class MaterialViewSet(ModelViewSet):
    """物料"""

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, MaterialPermission]
    filterset_fields = ['type', 'category']
    search_fields = ['number', 'name', 'remark']
    ordering_fields = ['id', 'number', 'name']
    select_related_fields = ['category']
    queryset = Material.objects.all()


class MaterialBillViewSet(ModelViewSet):
    """物料BOM"""

    serializer_class = MaterialBillSerializer
    permission_classes = [IsAuthenticated, MaterialBillPermission]
    filterset_fields = ['parent']
    search_fields = ['parent__number', 'parent__name']
    select_related_fields = ['parent', 'material']
    queryset = MaterialBill.objects.all()


__all__ = [
    'MaterialCategoryViewSet', 'MaterialViewSet', 'MaterialBillViewSet',
]
