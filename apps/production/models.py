from extensions.common.base import *
from extensions.models import *


class ProcessRoute(Model):
    """工艺路线"""

    material = ForeignKey('material.Material', on_delete=CASCADE,
                          related_name='process_route_set', verbose_name='物料')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='process_route_set')

    class Meta:
        unique_together = [('material', 'team')]


class Process(Model):
    """工序"""

    route = ForeignKey('production.ProcessRoute', on_delete=CASCADE,
                       related_name='process_set', verbose_name='路线')
    name = CharField(max_length=64, verbose_name='名称')
    index = IntegerField(verbose_name='步骤序号')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='process_set')


class ProductionOrder(Model):
    """生产单据"""

    class Status(TextChoices):
        """状态"""

        PLANNED = ('planned', '计划中')
        PUBLISHED = ('published', '已发布')
        CLOSED = ('closed', '已关闭')

    number = CharField(max_length=32, verbose_name='编号')
    material = ForeignKey('material.Material', on_delete=PROTECT,
                          related_name='production_order_set', verbose_name='物料')
    production_quantity = FloatField(verbose_name='生产数量')
    completed_quantity = FloatField(default=0, verbose_name='完成数量')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    status = CharField(max_length=32, choices=Status.choices, default=Status.PLANNED, verbose_name='状态')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='production_order_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    publish_time = DateTimeField(null=True, verbose_name='发布时间')
    close_time = DateTimeField(null=True, verbose_name='关闭时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='production_order_set')

    class Meta:
        unique_together = [('number', 'team')]


class ProductionProcess(Model):
    """生产工序"""

    production_order = ForeignKey('production.ProductionOrder', on_delete=CASCADE,
                                  related_name='production_process_set', verbose_name='生产单据')
    name = CharField(max_length=64, verbose_name='名称')
    index = IntegerField(verbose_name='步骤序号')
    start_time = DateTimeField(null=True, verbose_name='开始时间')
    end_time = DateTimeField(null=True, verbose_name='结束时间')
    completed_quantity = FloatField(default=0, verbose_name='完成数量')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='production_process_set')


class ProductionRecord(Model):
    """生产记录"""

    production_process = ForeignKey('production.ProductionProcess', on_delete=CASCADE,
                                    related_name='production_record_set', verbose_name='生产工序')
    production_order = ForeignKey('production.ProductionOrder', on_delete=CASCADE,
                                  related_name='production_record_set', verbose_name='生产单据')
    completed_quantity = FloatField(verbose_name='完成数量')
    working_hours = FloatField(null=True, verbose_name='工时')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='production_record_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='production_record_set')


__all__ = [
    'ProcessRoute', 'Process', 'ProductionOrder', 'ProductionProcess', 'ProductionRecord',
]
