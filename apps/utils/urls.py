from django.urls import include, path

from .api import urls as api_urls

urlpatterns = [
    path('api/auth/', include(api_urls.urlpatterns)),
]
