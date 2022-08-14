from django.db.models import Q, F, Prefetch
from django.db import transaction
from django.conf import settings
from functools import reduce
from decimal import Decimal
import pendulum
import re


class Number(Decimal):

    def __new__(cls, value, context=None) -> Decimal:
        return super().__new__(cls, value=str(value), context=context)


def get_next_number(last_number, default_number: str) -> str:
    """获取编号"""

    if not last_number or not (result := re.findall('[0-9]+', last_number)):
        return default_number

    current_number = result[-1]
    next_number = str(int(current_number) + 1)
    if len(current_number) > len(next_number):
        next_number = next_number.zfill(len(current_number))

    result = re.match(f'^(.*){current_number}(.*?)$', last_number)
    prefix, suffix = result[1], result[2]

    return prefix + next_number + suffix


__all__ = [
    'transaction', 'Q', 'F', 'Prefetch', 'settings', 'pendulum', 'reduce', 'Number', 'get_next_number',
]
