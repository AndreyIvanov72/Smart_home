from django.urls import path

from measurement.views import SensorView, SensorUpdateView, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='update_sensors'),
    path('measurements/', MeasurementCreateView.as_view(), name='create_measurement'),
]
