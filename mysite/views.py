from django.http import HttpResponse

import datetime

def current_datetime(request):
	
	now = datetime.datetime.now()
	html = "<html><boby>Fecha y hora actual del servidor %s.</body></html>"% now
	
	return HttpResponse(html)
