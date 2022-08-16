from extensions.common.base import *
from extensions.models import *


class QualityInspectionOrder(Model):
    """质检单据"""

    class Type(TextChoices):
        """类型"""

        INVENTORY_INSPECTION = ('inventory_inspection', '库存抽检')
        FIRST_INSPECTION = ('first_inspection', '首件抽检')
        DELIVERY_INSPECTION = ('delivery_inspection', '出货检验')

    class Status(TextChoices):
        """状态"""

        PLANNED = ('planned', '计划中')
        PUBLISHED = ('published', '已发布')

    number = CharField(max_length=32, verbose_name='编号')
    type = CharField(max_length=32, choices=Type.choices, verbose_name='类型')
    department = CharField(max_length=256, null=True, blank=True, verbose_name='部门')
    place = CharField(max_length=256, null=True, blank=True, verbose_name='地点')
    image_set = ManyToManyField('quality.QualityInspectionImage', blank=True,
                                related_name='quality_inspection_order_set', verbose_name='图片')
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


class QualityInspectionImage(Model):
    """质检图片"""

    file = ImageField(verbose_name='文件')
    name = CharField(max_length=64, verbose_name='名称')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='purchase_return_image_set')


__all__ = [
    'QualityInspectionOrder', 'QualityInspectionRecord',
]
