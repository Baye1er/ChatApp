from rest_framework import serializers
from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            #'first_name',
            #'last_name',
            'phone',
            #'email',
            'address',
            'profession',
            'age',
            'sex'
            #'profile'
        ]


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            #'firstname',
            #'lastname',
            'phone',
            #'e_mail',
            'address',
            'profession',
            'age',
            'sex'
            #'profile'
        ]