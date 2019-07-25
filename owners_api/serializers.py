from rest_framework import serializers
from owners_api.models import OwnerProfile
from drf_writable_nested import WritableNestedModelSerializer


class OwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProfile
        fields = ('salon_name', 'salon_address', 'salon_city',
                  'salon_state', 'salon_zip', 'salon_phone_number',
                  'salon_description')


class OwnerProfileSerializer(serializers.HyperlinkedModelSerializer):
    salon_profile = OwnerProfileSerializer(required=True)

    jobs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='job-detail',
    )

    class Meta:
        model = OwnerProfile
        fields = ('url', 'email', 'first_name', 'last_name',
                  'password', 'salon_profile', 'jobs')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('salon_profile')
        password = validated_data.pop('password')
        owner = OwnerProfile(**validated_data)
        owner.set_password(password)
        owner.save()
        # OwnerProfile.objects.create(owner=owner, **profile_data)
        return owner

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('salon_profile')
        profile = instance.salon_profile
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.salon_name = profile_data.get(
        'salon_name', profile.salon_name)
        profile.salon_address = profile_data.get(
            'salon_address', profile.salon_address)
        profile.salon_city = profile_data.get(
            'salon_city', profile.salon_city)
        profile.salon_state = profile_data.get(
            'salon_state', profile.salon_state)
        profile.salon_zip = profile_data.get(
            'salon_zip', profile.salon_zip)
        profile.salon_phone_number = profile_data.get(
            'salon_phone_number', profile.salon_phone_number)
        profile.salon_description = profile_data.get(
            'salon_description', profile.salon_description)

        profile.save()
        return instance
