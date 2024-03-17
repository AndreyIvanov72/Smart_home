from django.contrib import admin
from measurement.models import Sensor, Measurement
# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'get_sensor_name', 'get_sensor_description', 'temperature', 'created_at',)
    list_filter = ('sensor',)
    search_fields = ('sensor__name',)

    def get_sensor_name(self, obj):
        return obj.sensor.name

    get_sensor_name.short_description = 'Название'

    def get_id(self, obj):
        return obj.sensor.id

    get_id.short_description = 'ID'

    def get_sensor_description(self, obj):
        return obj.sensor.description

    get_sensor_description.short_description = 'Описание'
