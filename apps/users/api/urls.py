from apps.users.api.views import UserApiView, UserModelViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserModelViewSet, 'user')

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
    path(
        'me',
        UserApiView.as_view(),
        name='user_auth_me',
    )
]
