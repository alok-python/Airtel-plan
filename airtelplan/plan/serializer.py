from .models import AirtelPlan
from rest_framework import serializers



class AirtelSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=AirtelPlan
        fields='__all__'