from rest_framework import viewsets
from common.models import User
from owners_api.models import OwnerProfile
from owners_api.serializers import OwnerProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from jobs_api.models import Job
from jobs_api.serializers import JobSerializer
from rest_framework import permissions


class OwnerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = OwnerProfile.objects.all()
    serializer_class = OwnerProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' \
                or self.action == 'partial_update':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]


class OwnerJobList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):

        return Job.objects.filter(owner=self.kwargs['pk'])
