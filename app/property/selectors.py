from django.db.models import QuerySet
from property.models import Property
from property.constants import PropertyStatus
from django.contrib.auth.models import User
from typing import Optional


def filter_properties(
    *,
    year: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None
) -> QuerySet[PropertyStatus]:
    available_status = [tag.value for tag in PropertyStatus]
    filter_ = dict(status__in=available_status)
    if year:
        filter_ = dict(year=year)
    if city:
        filter_ = dict(city=city)
    if state:
        filter_ = dict(state=state)
    return Property.objects.filter(**filter_)


def filter_property_by_id(
    *,
    property_id: int
) -> QuerySet[PropertyStatus]:
    return Property.objects.filter(id=property_id)


def filter_user_by_id(
    *,
    user_id: int
) -> QuerySet[User]:
    return User.objects.filter(id=user_id)
