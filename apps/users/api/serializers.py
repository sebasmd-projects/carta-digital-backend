from apps.users.models import UserModel
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['__all__']

        read_only_fields = (
            "id",
            "last_login",
            "created",
            "updated"
        )