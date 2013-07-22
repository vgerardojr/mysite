from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><boby>It is now%s.</body></html>"% now
	return HttpResponse(html)
