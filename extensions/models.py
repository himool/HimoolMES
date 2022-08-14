from django.db.models import CharField, DateField, DateTimeField, JSONField, FileField, ImageField
from django.db.models import BooleanField, IntegerField, FloatField, DecimalField
from django.db.models import Sum, Count, Min, Avg, Max, Value, F, Q, Prefetch
from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT, PROTECT
from django.db.models import OneToOneField, ForeignKey, ManyToManyField
from django.db.models import Model, IntegerChoices, TextChoices
from django.db.models import QuerySet, Manager, ProtectedError
from extensions.exceptions import ValidationError
from django.db.models.functions import Coalesce
from django.db import connection
import pendulum


class AmountField(DecimalField):
    """金额字段"""

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_digits'], kwargs['decimal_places'] = 16, 2
        super().__init__(verbose_name, name, **kwargs)


class RefModel(Model):

    class RefManager(Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_deleted=False)

    is_deleted = BooleanField(default=False, verbose_name='删除状态')
    delete_time = DateTimeField(null=True, verbose_name='删除时间')

    objects = RefManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=None):
        try:
            super().delete(using, keep_parents)
        except ProtectedError as e:
            if self.is_deleted:
                raise ValidationError('数据已被引用, 无法彻底删除') from e

            self.is_deleted = True
            self.delete_time = pendulum.now().to_datetime_string()
            self.save(update_fields=['is_deleted', 'delete_time'])


__all__ = [
    'Model', 'RefModel', 'IntegerChoices', 'TextChoices',
    'CASCADE', 'SET_NULL', 'SET_DEFAULT', 'PROTECT',
    'OneToOneField', 'ForeignKey', 'ManyToManyField',
    'BooleanField', 'IntegerField', 'FloatField', 'AmountField',
    'CharField', 'DateField', 'DateTimeField', 'JSONField', 'FileField', 'ImageField',
    'Sum', 'Count', 'Min', 'Avg', 'Max', 'Value',
    'F', 'Q', 'Prefetch', 'Coalesce', 'connection',
]
