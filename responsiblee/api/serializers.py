from rest_framework import serializers
from .models import Emission

class EmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emission
        fields = ('emission_factor', 'co2_emission')