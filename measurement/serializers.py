from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)


class MeasurmentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fiellds = ['temperature', 'crearted_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurmentViewSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']