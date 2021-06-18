from .models import AgilePrinciple, AgileValue
from rest_framework import serializers


class AgilePrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgilePrinciple
        fields = ['id', 'field_value', 'created_at']


class AgileValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgileValue
        fields = ['id', 'field_value', 'created_at']