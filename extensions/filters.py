from django_filters.filters import NumberFilter, CharFilter, BooleanFilter, BaseInFilter, ChoiceField, MultipleChoiceFilter, DateFilter
from django_filters.rest_framework import FilterSet


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class CharInFilter(BaseInFilter, CharFilter):
    pass


__all__ = [
    'FilterSet', 'NumberInFilter', 'CharInFilter', 'DateFilter',
    'NumberFilter', 'CharFilter', 'BooleanFilter', 'BaseInFilter', 'ChoiceField', 'MultipleChoiceFilter',
]
