from extensions.common.schema import *
from extensions.common.base import *
from extensions.permissions import *
from extensions.exceptions import *
from extensions.viewsets import *
from apps.production.serializers import *
from apps.production.permissions import *
from apps.production.filters import *
from apps.production.schemas import *
from apps.production.models import *


class ProcessRouteViewSet(ModelViewSet):
    """工艺路线"""

    serializer_class = ProcessRouteSerializer
    permission_classes = [IsAuthenticated, ProcessRoutePermission]
    filterset_fields = ['material']
    search_fields = ['remark']
    select_related_fields = ['material']
    prefetch_related_fields = ['process_set']
    queryset = ProcessRoute.objects.all()


__all__ = [

]
