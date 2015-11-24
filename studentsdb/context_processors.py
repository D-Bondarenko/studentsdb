from .settings import PORTAL_URL

def studets_proc(request):
	return ({'PORTAL_URL':PORTAL_URL})