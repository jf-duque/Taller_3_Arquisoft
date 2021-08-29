from ..models import Measurement 

def get_all_measurements():
	measurements = Measurement.objects.all()
	return measurements

def get_measurement_by_id(pPk):
	measurement = Measurement.objects.get(pk=pPk)
	return measurement

def delete_measurement_by_id(pPk):
	measurement = Measurement.objects.get(pk=pPk).delete()
	identificador = "% s" % pPk
	return ('la medida con id = ' + identificador + ' fue borrada.')

def modificar_measurement_by_id(pPk, pValue):
	measurement = Measurement.objects.get(pk=pPk)
	measurement.modifyValue(pValue)
	identificador = "% s" % pPk
	nValue = "% s" % pValue
	return ('la medida con id = ' + identificador + ' fue modificada por: ' + nValue)



