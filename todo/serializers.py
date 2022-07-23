from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
            "is_complete",
            "date_created",
        )
        read_only_fields = ("is_complete",)
