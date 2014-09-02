# -*- coding: utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from fda.models import ExpertStatement as ES

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
	

	es = ES.objects.all()
	for obj in jsonObject:
		for s in es:
			#print obj['name'] + " " + s.foodName
			if obj['name'] == s.foodName:

				obj['statement'] = s.statement
	sortedJsonList = sorted(jsonObject, key=lambda k: -k['radius']) 
	return render(request,"fda/feedback.html",{"data":sortedJsonList})




def editExpertStatement(request):
	es = request.POST

	try:
		e = ES.objects.get(foodName = es['foodName'])
		e.statement = es['statement']
	except ES.DoesNotExist:
		e = ES(foodName=es['foodName'],statement=es['statement'])

	e.save()

	return HttpResponse("editExpertStatement success")

#expert statement api

@csrf_exempt
def getExpertStatement(request):
	element = request.POST.get('ElementName',False)
	try:
		e = ES.objects.get(foodName = element)
		data = data = {"ExpertStatement":e.statement}
	except ES.DoesNotExist:
		data ={"Error_Msg": "No data"}

	#for testing
	if element == "demoFood":
		 data = {"ExpertStatement":"不建議過量攝取此添加物."}
	return HttpResponse(json.dumps(data,ensure_ascii = False),content_type="application/json; charset=utf-8")












