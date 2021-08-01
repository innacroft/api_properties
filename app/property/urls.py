from django.urls import path

from property import views

app_name = 'property'
urlpatterns = [
    path(
        'properties/',
        views.PropertiesView.as_view(),
        name='properties'
    ),
    path(
        'like/',
        views.LikePropertiesView.as_view(),
        name='like-properties'
    ),
    path(
        'authenticator/',
        views.UserAuth.as_view(),
        name='authentication-user'
    )
]