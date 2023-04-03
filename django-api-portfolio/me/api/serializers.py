from me.models import Me
from django.conf import settings
from rest_framework import serializers


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Me
        fields = '__all__'
        