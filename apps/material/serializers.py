from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.material.models import *


class MaterialCategorySerializer(BaseSerializer):

    class Meta:
        model = MaterialCategory
        read_only_fields = ['id']
        fields = ['name', 'remark', *read_only_fields]
        validators = [TeamUniqueValidator(fields=['name'], message='名称已存在')]


class MaterialSerializer(BaseSerializer):

    class CategoryItemSerializer(BaseSerializer):

        class Meta:
            model = MaterialCategory
            fields = ['id', 'name']
            ref_name = 'material.MaterialSerializer.CategoryItemSerializer'

    type_display = CharField(source='get_type_display', read_only=True, label='类型')
    category_item = CategoryItemSerializer(source='category', read_only=True, label='分类Item')

    class Meta:
        model = Material
        read_only_fields = ['id', 'type_display', 'category_item']
        fields = ['number', 'name', 'type', 'category', 'spec', 'unit', 'remark', *read_only_fields]
        validators = [TeamUniqueValidator(fields=['number'], message='名称已被注册')]


class MaterialBillSerializer(BaseSerializer):

    class MaterialItemSerializer(BaseSerializer):

        class Meta:
            model = Material
            fields = ['id', 'number', 'name', 'spec', 'unit']
            ref_name = 'material.MaterialBillSerializer.MaterialItemSerializer'

    finish_product_item = MaterialItemSerializer(source='finish_product', read_only=True, label='成品Item')
    raw_material_item = MaterialItemSerializer(source='raw_material', read_only=True, label='原料Item')

    class Meta:
        model = MaterialBill
        read_only_fields = ['id', 'finish_product_item', 'raw_material_item']
        fields = ['finish_product', 'raw_material', 'quantity', 'remark', *read_only_fields]


__all__ = [
    'MaterialCategorySerializer', 'MaterialSerializer', 'MaterialBillSerializer',
]
