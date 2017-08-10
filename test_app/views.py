from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.sessions.models import Session

from django.shortcuts import render
#import loggings

from django.http import HttpResponseRedirect, HttpResponse
from django_auth_ldap.backend import LDAPBackend

"""
def index(request):
    session = Session.objects.all().first()

    return render_to_response(
        'index.html',
        {'session_info': None if session is None else session.get_decoded()},
        context_instance=RequestContext(request)
    )
"""
def index2(request):
	msj = "Hello index"
	return render(request, 'index.html', {'msj': msj,})
	#return HttpResponse(template.render(context, request))

def index3(request):
	msj = "Hello index"
	return render(request, 'login.html', {'msj': msj,})
	#return HttpResponse(template.render(context, request))
