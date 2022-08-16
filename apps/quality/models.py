from extensions.common.base import *
from extensions.models import *


class QualityInspectionOrder(Model):
    """质检单据"""

    class Status(TextChoices):
        """状态"""

        PLANNED = ('planned', '计划中')
        PUBLISHED = ('published', '已发布')

    number = CharField(max_length=32, verbose_name='编号')
    department = CharField(max_length=256, null=True, blank=True, verbose_name='部门')
    place = CharField(max_length=256, null=True, blank=True, verbose_name='地点')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    status = CharField(max_length=32, choices=Status.choices, default=Status.PLANNED, verbose_name='状态')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='quality_inspection_order_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    publish_time = DateTimeField(null=True, verbose_name='发布时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='quality_inspection_order_set')

    class Meta:
        unique_together = [('number', 'team')]


class QualityInspectionRecord(Model):
    """质检记录"""

    quality_inspection_order = ForeignKey('quality.QualityInspectionOrder', on_delete=CASCADE,
                                          related_name='quality_inspection_record_set', verbose_name='质检单据')
    feedback = CharField(max_length=256, null=True, blank=True, verbose_name='反馈')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='quality_inspection_record_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='quality_inspection_record_set')


__all__ = [
    'QualityInspectionOrder', 'QualityInspectionRecord',
]
