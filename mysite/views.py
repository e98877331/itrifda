from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
#    return HttpResponse('yaya get it')
    return render(request, 'mysite/index.html', {})

