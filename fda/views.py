from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your views here.

dataPath = "{0}/../fda/data/dd.json".format(settings.PROJECT_ROOT)

def index(request):
    return render(request,"fda/index.html", {})


def showGraph(request):
	return render(request,"fda/graph1.html",{})

def genData(request):
    path = "{0}/../fda/data/test.json".format(settings.PROJECT_ROOT)
    with open(path, "w") as out:
        out.write("testing data") 

    return HttpResponse("success generate data")
   
def getGraphData(request):

	fp = open(dataPath, "r")
	json = fp.read()
	return HttpResponse(json)


def showGraph2(request):
	print "go graph 2"
	return render(request,"fda/graph2.html",{})


def genData2(request):
    path = "{0}/../fda/data/graph2.json".format(settings.PROJECT_ROOT)
    with open(path, "w") as out:
        out.write("testing data") 

    return HttpResponse("success generate data")
   
def getGraphData2(request):
	dataPath = "{0}/../fda/data/g2.json".format(settings.PROJECT_ROOT)
	fp = open(dataPath, "r")
	json = fp.read()
	return HttpResponse(json)
