from rest_framework import serializers
from stylists_api.models import StylistProfile

class StylistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StylistProfile
        fields = ('phone_number', 'years_experience', 'licenses',
                  'photo1',
                  'photo2', 'photo3', 'photo4', 'photo5', 'photo6',
                  'specializations')

class StylistSerializer(serializers.HyperlinkedModelSerializer):
    stylist_profile = StylistProfileSerializer(required=True)

    class Meta:
        model = StylistProfile
        fields = ('url', 'email', 'first_name', 'last_name',
                  'password', 'stylist_profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('stylist_profile')
        password = validated_data.pop('password')
        stylist = StylistProfile(**validated_data)
        stylist.set_password(password)
        stylist.save()
        # StylistProfile.objects.create(stylist=stylist, **profile_data)
        return stylist

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('stylist_profile')
        profile = instance.stylist_profile
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone_number = profile_data.get('phone_number',
                                                profile.phone_number)
        profile.years_experience = profile_data.get(
            'years_experience', profile.years_experience)
        profile.licenses = profile_data.get('licenses',
                                            profile.licenses)
        profile.photo1 = profile_data.get('photo1', profile.photo1)
        profile.photo2 = profile_data.get('photo2', profile.photo2)
        profile.photo3 = profile_data.get('photo3', profile.photo3)
        profile.photo4 = profile_data.get('photo4', profile.photo4)
        profile.photo5 = profile_data.get('photo5', profile.photo5)
        profile.photo6 = profile_data.get('photo6', profile.photo6)
        profile.specializations = profile_data.get(
            'specializations', profile.specializations)
        profile.save()
        return instance
