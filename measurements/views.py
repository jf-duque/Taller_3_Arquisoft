from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_by_id, delete_measurement_by_id, modificar_measurement_by_id
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
	measurements = get_all_measurements()
	measurements_list = serializers.serialize('json', measurements)
	return HttpResponse	(measurements_list, content_type='application/json')

def getById(request, pPk):
	measurement = get_measurement_by_id(pPk)
	# measurements_byid = serializers.serialize('json', measurement)
	return HttpResponse (measurement, content_type='application/json')
	# return HttpResponse ("llego al metodo")

def deleteById(request, pPk):
	measurement = delete_measurement_by_id(pPk)
	return HttpResponse(measurement)

def modificarById(request, pPk, pValue):	
	measurement = modificar_measurement_by_id(pPk, pValue)
	return HttpResponse(measurement)


# Create your views here.
