from rest_framework.relations import RelatedField, ManyRelatedField, MANY_RELATION_KWARGS
from rest_framework.fields import SerializerMethodField, ImageField, FileField, JSONField
from rest_framework.fields import IntegerField, FloatField, DecimalField, BooleanField
from rest_framework.validators import UniqueTogetherValidator, qs_exists
from rest_framework.fields import CharField, DateField, DateTimeField
from rest_framework.serializers import Serializer, ModelSerializer
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from extensions.exceptions import ValidationError
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes


class TeamUniqueValidator(UniqueTogetherValidator):

    def __init__(self, fields, message=None):
        self.fields = fields
        self.message = message or self.message

    def __call__(self, attrs, serializer):
        queryset = serializer.Meta.model.objects.filter(team=serializer.team)
        self.enforce_required_fields(attrs, serializer)
        queryset = self.filter_queryset(attrs, queryset, serializer)
        queryset = self.exclude_current_instance(attrs, queryset, serializer.instance)

        # Ignore validation if any field is None
        checked_values = [
            value for field, value in attrs.items() if field in self.fields
        ]

        if None not in checked_values and qs_exists(queryset):
            raise ValidationError(self.message, code='unique')


@extend_schema_field(OpenApiTypes.DECIMAL)
class AmountField(DecimalField):
    """金额字段"""

    def __init__(self, coerce_to_string=None, max_value=None, min_value=None, localize=False,
                 rounding=None, **kwargs):

        kwargs['max_digits'], kwargs['decimal_places'] = 16, 2
        super().__init__(coerce_to_string=coerce_to_string, max_value=max_value, min_value=min_value,
                         localize=localize, rounding=rounding, **kwargs)


class _ManyRelatedField(ManyRelatedField):
    default_error_messages = {
        'not_a_list': _('Expected a list of items but got type "{input_type}".'),
        'does_not_exist': _('Invalid pk "{pk_value}" - object does not exist.'),
        'empty': _('This list may not be empty.')
    }

    def to_internal_value(self, data):
        if isinstance(data, str) or not hasattr(data, '__iter__'):
            self.fail('not_a_list', input_type=type(data).__name__)
        if not self.allow_empty and len(data) == 0:
            self.fail('empty')

        queryset = self.child_relation.get_queryset()
        instance_set = queryset.filter(pk__in=data)

        if len(data) != len(instance_set):
            self.fail('does_not_exist', pk_value=set(data) - {instance.pk for instance in instance_set})
        return instance_set


class _RelatedField(RelatedField):

    @property
    def team(self):
        return self.context['request'].user.team

    @property
    def user(self):
        return self.context['request'].user

    @classmethod
    def many_init(cls, *args, **kwargs):
        list_kwargs = {key: kwargs[key] for key in kwargs if key in MANY_RELATION_KWARGS}
        list_kwargs['child_relation'] = cls(*args, **kwargs)
        return _ManyRelatedField(**list_kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(team=self.team)


@extend_schema_field(OpenApiTypes.INT)
class ForeignKeyField(_RelatedField):
    default_error_messages = {
        'required': _('This field is required.'),
        'does_not_exist': _('Invalid pk "{pk_value}" - object does not exist.'),
        'incorrect_type': _('Incorrect type. Expected pk value, received {data_type}.'),
    }

    def __init__(self, **kwargs):
        self.pk_field = kwargs.pop('pk_field', None)
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return True

    def to_internal_value(self, data):
        if self.pk_field is not None:
            data = self.pk_field.to_internal_value(data)
        queryset = self.get_queryset()
        try:
            if isinstance(data, bool):
                raise TypeError
            return queryset.get(pk=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)

    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)
        return value.pk


class BaseSerializer(ModelSerializer):

    serializer_related_field = ForeignKeyField

    @property
    def request(self):
        return self.context['request']

    @property
    def team(self):
        return self.context['request'].user.team

    @property
    def user(self):
        return self.context['request'].user

    def create(self, validated_data):
        validated_data['team'] = self.team
        return super().create(validated_data)


__all__ = [
    'Serializer', 'BaseSerializer',
    'SerializerMethodField', 'ImageField', 'FileField', 'JSONField',
    'BooleanField', 'IntegerField', 'FloatField', 'AmountField',
    'CharField', 'DateField', 'DateTimeField', 'ForeignKeyField',
    'TeamUniqueValidator',
]
