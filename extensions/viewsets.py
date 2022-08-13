from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from extensions.paginations import BasePagination
from rest_framework.viewsets import ViewSet


class FunctionViewSet(ViewSet):
    """功能视图"""

    @property
    def team(self):
        return self.request.user.team

    @property
    def user(self):
        return self.request.user

    @property
    def context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}


class BaseViewSet(GenericViewSet):
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']
    select_related_fields = []
    prefetch_related_fields = []

    @property
    def team(self):
        return self.request.user.team

    @property
    def user(self):
        return self.request.user

    @property
    def context(self):
        return self.get_serializer_context()

    def get_queryset(self):
        queryset = super().get_queryset().filter(team=self.team)
        queryset = queryset.select_related(*self.select_related_fields)
        queryset = queryset.prefetch_related(*self.prefetch_related_fields)
        return queryset


class ListViewSet(BaseViewSet, ListModelMixin):
    """列表视图"""

    pagination_class = None


class PagingViewSet(BaseViewSet, ListModelMixin):
    """分页视图"""


class ReadOnlyViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin):
    """只读视图"""


class ModelViewSet(BaseViewSet, ListModelMixin, CreateModelMixin,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    """模型视图"""


__all__ = [
    'ListModelMixin', 'CreateModelMixin', 'RetrieveModelMixin', 'UpdateModelMixin', 'DestroyModelMixin',
    'DjangoFilterBackend', 'SearchFilter', 'OrderingFilter',
    'FunctionViewSet', 'BaseViewSet', 'ListViewSet', 'PagingViewSet', 'ReadOnlyViewSet', 'ModelViewSet',
]
