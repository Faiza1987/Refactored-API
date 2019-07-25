from django.urls import path, include
from owners_api.views import OwnerViewSet
from owners_api.views import OwnerJobList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('owners/<pk>/jobs', OwnerJobList.as_view())
]
