from rest_framework import serializers
from property.models import Property

class InputPropertiesSerializer(serializers.Serializer):
    year = serializers.CharField(required=False, allow_blank=True, max_length=100)
    city = serializers.CharField(required=False, allow_blank=True, max_length=100)
    state = serializers.CharField(required=False, allow_blank=True, max_length=100)


class OutputPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'city', 'state', 'price', 'description']


