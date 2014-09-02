# -*- coding: utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt

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


def feedback(request):
	dataPath = "{0}/../fda/data/g2.json".format(settings.PROJECT_ROOT)
	fp = open(dataPath, "r")
	jsonString = fp.read()
	jsonObject = json.loads(jsonString)

	return render(request,"fda/feedback.html",{"data":jsonObject})

#expert statement api

@csrf_exempt
def getExpertStatement(request):
	element = request.POST.get('ElementName',False)
	print element
	if element:
		if element == "": 
			data ={"Error_Msg": "No data"}
		else:
			data = {"ExpertStatement":"一天不要吃太多! 建議配水服用"}
	else:
		data ={"Error_Msg": "No data"}
	return HttpResponse(json.dumps(data,ensure_ascii = False),content_type="application/json; charset=utf-8")












