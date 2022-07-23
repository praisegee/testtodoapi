from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label="Create password", min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "fullname",
            "username",
            "email",
            "password",
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label="Password", min_length=6, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "fullname",
            "username",
            "email",
            "password",
            "token",
        )
        read_only_fields = ("fullname", "username", "token", "id")

    def get_token(self, obj):
        return obj.auth_token.key

