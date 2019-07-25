from rest_framework import viewsets
from common.models import User
from stylists_api.serializers import StylistSerializer
from rest_framework.permissions import AllowAny
from stylists_api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from stylists_api.models import StylistProfile


class StylistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = StylistProfile.objects.all()
    serializer_class = StylistSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' \
                or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


