from rest_framework import serializers

from user.models import *


class UserSerializer(serializers.ModelSerializer):
    '''
        In Django REST Framework, the class Meta within a serializer is used to configure aspects of
        the serializer's behavior. It provides metadata about the serializer,
        such as the model it's associated with and the fields to include or exclude.
    '''
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'email', 'password']