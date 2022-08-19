from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.production.models import *
from apps.material.models import *


class ProcessRouteSerializer(BaseSerializer):

    class MaterialItemSerializer(BaseSerializer):

        class Meta:
            model = Material
            fields = ['id', 'number', 'name', 'spec', 'unit']
            ref_name = 'production.ProcessRouteSerializer.MaterialItemSerializer'

    class ProcessItemSerializer(BaseSerializer):
        id = IntegerField(required=False, label='ID')

        class Meta:
            model = Process
            fields = ['id', 'name', 'index', 'remark']
            ref_name = 'production.ProcessRouteSerializer.ProcessItemSerializer'

    material_item = MaterialItemSerializer(source='material', many=True, read_only=True, label='物料Item')
    process_items = ProcessItemSerializer(source='process_set', many=True, label='工序Items')

    class Meta:
        model = ProcessRoute
        read_only_fields = ['id', 'material_item']
        fields = ['material', 'remark', 'process_items', *read_only_fields]
        validators = [TeamUniqueValidator(fields=['material'], message='物料的工艺路线已存在')]

    def create(self, validated_data):
        process_items = validated_data.pop('process_items')
        process_route = super().create(validated_data)

        Process.objects.bulk_create([Process(team=self.team, route=process_route, name=process_item['name'],
                                             index=process_item['index'], remark=process_item.get('remark'))
                                     for process_item in process_items])

        return process_route

    def update(self, instance, validated_data):
        process_items = validated_data.pop('process_items')
        process_route = super().update(instance, validated_data)

        create_process_set = []
        update_process_set = []
        for process_item in process_items:
            # 更新对象
            if process_id := process_item.get('id'):
                if process := Process.objects.filter(id=process_id, route=process_route).first():
                    update_process_set.append(process)
                    process.name = process_item['name']
                    process.index = process_item['index']
                    process.remark = process_item.get('remark')
                    continue

            # 新增对象
            create_process_set.append(Process(team=self.team, route=process_route, name=process_item['name'],
                                              index=process_item['index'], remark=process_item.get('remark')))

        Process.objects.filter(route=process_route).exclude(id__in=update_process_set).delete()
        Process.objects.bulk_update(update_process_set, ['name', 'index', 'remark'])
        Process.objects.bulk_create(create_process_set)

        return process_route


__all__ = [
    'ProcessRouteSerializer',
]
