from extensions.common.base import *
from extensions.models import *


class MaterialCategory(Model):
    """物料分类"""

    name = CharField(max_length=64, verbose_name='名称')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='material_category_set')

    class Meta:
        unique_together = [('name', 'team')]


class Material(RefModel):
    """物料"""

    class Type(TextChoices):
        """类型"""

        RAW_MATERIAL = ('raw_material', '原材料')
        FINISHED_PRODUCT = ('finished_product', '成品')

    number = CharField(max_length=32, verbose_name='编号')
    name = CharField(max_length=64, verbose_name='名称')
    type = CharField(max_length=32, choices=Type.choices, verbose_name='类型')
    category = ForeignKey('material.MaterialCategory', on_delete=SET_NULL, null=True,
                          related_name='material_set', verbose_name='分类')
    spec = CharField(max_length=64, null=True, blank=True, verbose_name='规格')
    unit = CharField(max_length=64, null=True, blank=True, verbose_name='单位')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='material_set')

    class Meta:
        unique_together = [('number', 'team')]


class MaterialBill(Model):
    """物料BOM"""

    parent = ForeignKey('material.Material', on_delete=CASCADE,
                        related_name='bill_material_set', verbose_name='父类')
    material = ForeignKey('material.Material', on_delete=CASCADE,
                          related_name='material_bill_set', verbose_name='物料')
    quantity = FloatField(verbose_name='数量')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='material_set')


__all__ = [
    'MaterialCategory', 'Material', 'MaterialBill',
]
