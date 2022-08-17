from extensions.permissions import *


class MaterialCategoryPermission(ModelPermission):
    code = 'material_category'


class MaterialPermission(ModelPermission):
    code = 'material'


class MaterialBillPermission(ModelPermission):
    code = 'material_bill'


__all__ = [
    'MaterialCategoryPermission', 'MaterialPermission', 'MaterialBillPermission',
]
