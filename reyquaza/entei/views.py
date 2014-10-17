from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))

def search_extension(request, extension_name):
    a = 2
    return render_to_response("index.html", context_instance=RequestContext(request))
