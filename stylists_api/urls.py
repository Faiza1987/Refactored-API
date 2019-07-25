from django.urls import path, include
from rest_framework import routers
from stylists_api.views import StylistViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('stylists', StylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]


