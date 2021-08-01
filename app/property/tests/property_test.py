from pytest_bdd import scenarios, given, when, then, parsers
from property.models import Property
from rest_framework.test import APIClient

scenarios('property_test.feature')


@given(
    parsers.parse('I create property with year "{year}" city "{city}" state "{state}"')
)
def create_property(
    year,
    city,
    state
):
    Property.objects.create(year=year, city=city, state=state)


@given(
    parsers.parse('I call service with year "{year}"'), target_fixture='response_req'
)
def call_endpoint(
    year
):
    ENPOINT = '/properties/'
    client = APIClient()
    response = client.post(
        ENPOINT,
        data=dict(year=year),
        format='json'

    )
    return response


@given(
    parsers.parse('I call service with city "{city}"'), target_fixture='response_req'
)
def call_endpoint1(
    city
):
    ENPOINT = '/properties/'
    client = APIClient()
    response = client.post(
        ENPOINT,
        data=dict(city=city),
        format='json'

    )
    return response


@given(
    parsers.parse('I call service with state "{state}"'), target_fixture='response_req'
)
def call_endpoint1(
    state
):
    ENPOINT = '/properties/'
    client = APIClient()
    response = client.post(
        ENPOINT,
        data=dict(state=state),
        format='json'

    )
    return response

@then(
    parsers.parse('Response status code is "{code}"')
)
def response_status(
    code,
    response_req
):
    assert response_req.status_code == code