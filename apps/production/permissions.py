from extensions.permissions import *


class ProcessRoutePermission(ModelPermission):
    code = 'process_route'


__all__ = [
    'ProcessRoutePermission',
]
