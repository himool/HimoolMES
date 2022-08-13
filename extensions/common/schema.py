from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework.decorators import action
from extensions.serializers import *
from rest_framework import status


class MakeNumberResponse(Serializer):
    number = CharField(label='编号')


__all__ = [
    'extend_schema', 'OpenApiParameter', 'OpenApiResponse', 'OpenApiTypes',
    'Response', 'action', 'status',
    'MakeNumberResponse',
]
