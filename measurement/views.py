from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()


class SensorUpdateView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()
    lookup_field= 'pk'