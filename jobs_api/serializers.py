from rest_framework import serializers
from jobs_api.models import Job
from owners_api.models import OwnerProfile


class JobSerializer(serializers.ModelSerializer):

    owner = serializers.HyperlinkedRelatedField(
        view_name="ownerprofile-detail",
        default=serializers.CurrentUserDefault(),
        queryset=OwnerProfile.objects.all(),
    )

    class Meta:
        model = Job
        fields = ('url', "title", "hourly_rate", "company", "address", "city", "state", "zip_code",
                  "description", "contact_email", "owner")
