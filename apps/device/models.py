from extensions.common.base import *
from extensions.models import *


class DeviceCategory(Model):
    """设备分类"""

    name = CharField(max_length=64, verbose_name='名称')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='device_category_set')

    class Meta:
        unique_together = [('name', 'team')]


class Device(Model):
    """设备"""

    number = CharField(max_length=32, verbose_name='编号')
    name = CharField(max_length=64, verbose_name='名称')
    category = ForeignKey('device.DeviceCategory', on_delete=SET_NULL, null=True,
                          related_name='device_set', verbose_name='分类')
    spec = CharField(max_length=64, null=True, blank=True, verbose_name='规格')
    supplier = CharField(max_length=64, null=True, blank=True, verbose_name='供应商')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='device_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='device_set')

    class Meta:
        unique_together = [('number', 'team')]


class SparePart(Model):
    """备件"""

    number = CharField(max_length=32, verbose_name='编号')
    name = CharField(max_length=64, verbose_name='名称')
    spec = CharField(max_length=64, null=True, blank=True, verbose_name='规格')
    unit = CharField(max_length=64, null=True, blank=True, verbose_name='单位')
    unit_price = FloatField(null=True, verbose_name='单价')
    min_quantity = FloatField(null=True, verbose_name='最低库存')
    total_quantity = FloatField(null=True, verbose_name='库存总数')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='spare_part_set')

    class Meta:
        unique_together = [('number', 'team'), ('name', 'team')]


class PatrolInspectionTask(Model):
    """巡检任务"""

    device = ForeignKey('device.Device', on_delete=PROTECT,
                        related_name='patrol_inspection_task_set', verbose_name='设备')
    inspection_part = CharField(max_length=64, null=True, blank=True, verbose_name='检查部位')
    evaluation_basis = CharField(max_length=256, null=True, blank=True, verbose_name='评定基准')
    execution_cycle = CharField(max_length=64, null=True, blank=True, verbose_name='执行周期')
    execution_sequence = CharField(max_length=256, null=True, blank=True, verbose_name='执行顺序')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='patrol_inspection_task_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='patrol_inspection_task_set')


class PatrolInspectionRecord(Model):
    """巡检记录"""

    class Status(TextChoices):
        """状态"""

        NORMAL = ('normal', '正常运行')
        FAIL_SAFE = ('fail_safe', '带病运行')
        STANDBY_MAINTENANCE = ('standby_maintenance', '待机维修')
        SCRAP = ('scrap', '报废')
        DEACTIVATION = ('deactivation', '停用')

    patrol_inspection_task = ForeignKey('device.PatrolInspectionTask', on_delete=CASCADE,
                                        related_name='patrol_inspection_record_set', verbose_name='巡检任务')
    status = CharField(max_length=32, choices=Status.choices, verbose_name='状态')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='patrol_inspection_record_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='patrol_inspection_record_set')


class RepairTask(Model):
    """维修任务"""

    device = ForeignKey('device.Device', on_delete=PROTECT,
                        related_name='repair_task_set', verbose_name='设备')
    failure_time = DateTimeField(null=True, verbose_name='故障时间')
    fault_phenomenon = CharField(max_length=256, null=True, blank=True, verbose_name='故障现象')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='repair_task_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='repair_task_set')


class RepairRecord(Model):
    """维修记录"""

    repair_task = ForeignKey('device.RepairTask', on_delete=CASCADE,
                             related_name='repair_record_set', verbose_name='维修任务')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='repair_record_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='repair_record_set')


class MaintenanceTask(Model):
    """维保任务"""

    device = ForeignKey('device.Device', on_delete=PROTECT,
                        related_name='maintenance_task_set', verbose_name='设备')
    execution_cycle = CharField(max_length=64, null=True, blank=True, verbose_name='执行周期')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='maintenance_task_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='maintenance_task_set')


class MaintenanceRecord(Model):
    """维保任务"""

    maintenance_task = ForeignKey('device.MaintenanceTask', on_delete=CASCADE,
                                  related_name='maintenance_record_set', verbose_name='维保任务')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='maintenance_record_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='maintenance_record_set')


class DeviceStatus(Model):
    """设备状态"""

    class Status(TextChoices):
        """状态"""

        RUNNING = ('running', '运行')
        SHUTDOWN = ('shutdown', '停机')
        FAILURE = ('failure', '故障')

    device = ForeignKey('device.Device', on_delete=PROTECT,
                        related_name='device_status_set', verbose_name='设备')
    status = CharField(max_length=32, choices=Status.choices, verbose_name='状态')
    start_time = DateTimeField(null=True, verbose_name='开始时间')
    end_time = DateTimeField(null=True, verbose_name='结束时间')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='device_status_set', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='device_status_set')


__all__ = [
    'DeviceCategory', 'Device', 'SparePart', 'PatrolInspectionTask', 'PatrolInspectionRecord',
    'RepairTask', 'RepairRecord', 'MaintenanceTask', 'MaintenanceRecord', 'DeviceStatus',
]
