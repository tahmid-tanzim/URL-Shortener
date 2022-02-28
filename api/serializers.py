from rest_framework import serializers
from .models import TinyURL


class TinyURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinyURL
        fields = "__all__"
