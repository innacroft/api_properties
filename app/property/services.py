from typing import Optional
from property import selectors
from rest_framework.exceptions import APIException
from property.constants import PropertyStatus
from django.db.models import QuerySet
from property.models import PropertyCustomer


def search_properties(
    *,
    year: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None
) -> QuerySet[PropertyStatus]:
    qr_property = selectors.filter_properties(
        year=year,
        city=city,
        state=state
    ).values('address', 'city', 'state', 'price', 'description')
    if not qr_property.exists():
        raise APIException(
            f'Properties with specification '
            f'are not avaliable year {year},city {city},'
            f'state {state} ')
    return qr_property


def like_properties(
    *,
    user_id: int,
    property_id: int
) -> None:
    qr_property = selectors.filter_property_by_id(
        property_id=property_id
    ).values('id')
    if not qr_property.exists():
        raise APIException(
            f'Property doesnt exists'
        )
    qr_user = selectors.filter_user_by_id(
        user_id=user_id
    ).values('id')
    if not qr_user.exists():
        raise APIException(
            f'User doesnt exists'
        )

    save_like = PropertyCustomer.objects.create(
        property_id=qr_property.first().get('id'),
        user_id=qr_user.first().get('id')
    )
    if not save_like:
        raise APIException(
            f'Something went wrong trying to save like'
        )
