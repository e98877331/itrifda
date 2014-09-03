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

	dataPath = "{0}/../fda/data/g2.json".format(settings.PROJECT_ROOT)
	fp = open(dataPath, "r")
	jsonString = fp.read()
	jsonObject = json.loads(jsonString)
	sortedJsonList = sorted(jsonObject, key=lambda k: -k['radius']) 
	return render(request,"fda/graph2.html",{"data":sortedJsonList})


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
		 data = {"ExpertStatement":'''菊糖(inulin)是一種來自菊芋的萃取物，由8~9個果糖聚合而成的多醣類，在末端以β-(1→2)的方式鍵結成為異果寡糖，人類並沒有分解此結構的酵素，這種異果寡糖無法被人體消化吸收，是屬於水溶性膳食纖維的一種。

但這種對人體無營養價值的膳食纖維，在腸道中卻被有益菌視為營養來源而大快朵頤，因為有益菌可以分解、利用異果寡糖，作為其生長的營養來源。

進而繁延更多的有益菌，抑制了壞菌的生長，維持腸道的健康環境。再加上菊糖低熱量的特性，添加在幼童的營養補充品中，除了可以對腸胃道有所助益外，也可以避免因為攝取過多的蔗糖造成的肥胖，讓幼童在成長過程中，更有效的吸收及利用營養。

菊糖inulin（菊苣纖維）由菊苣根部所萃取出來，因此也可稱為菊苣纖維，屬於可溶於水中的膳食纖維膳食纖維可促進腸道蠕動，讓排便順暢，並增加飽足感具降低血脂及調節腸胃道菌相等生理功效∼
菊苣所特有的天然Oligo寡糖，內含豐富的Bifidus菌，不容易在胃部被分解破壞，所以可以完整的到達腸道，幫助腸道蠕動。

菊 糖是一種天然存在於超過三萬多種植物及蔬菜中的多醣體。菊苣纖維是由菊苣（一種植物）球莖中萃取出來的菊糖，屬於水溶性膳食纖維，無法在胃或小腸被分解或 消化，可完整進入大腸做為益菌的養分。大腸內有許多不同的菌種，菊糖具選擇性地刺激某些益菌的生長（如，Bifidus bacteria），做為益菌的養分及生長基質，藉由平衡大腸內菌叢生態以達到促進身體健康的功能。
菊苣纖維的甜度是蔗糖的10%，與代糖合用有加成效果，可修飾代糖而提供較圓潤自然的味道。用於取代脂肪，或改良低脂或低糖、低熱量產品的口感及滑順感效果極佳。
由於在消化系統中不被分解消化，因此不會使血糖上升也不會影響胰島素分泌，當然也就具備了糖尿病可食及低熱量的特色。

各類食品原料中，如奶粉、優酪乳等都可以見到「菊糖」這個成分，菊糖和一般糖類有何不同？
所謂菊糖(Inulin)廣泛地存在於多種蔬果(如香蕉、蕃茄、洋蔥)中的果寡糖(Fructo-oligosaccharides)成分，在歐美地區被當作是食品原料而使用於各類食品中。
由於菊糖(inulin)本身是一種來自菊芋的萃取物，由8~9個果糖聚合而成的多醣類，在末端以β-(1→2)的方式鍵結成為異果寡糖。但是人類並沒有分解此結構的酵素，使得異果寡糖無法被人體消化吸收，屬於水溶性膳食纖維的一種。
既然無法被人體消化吸收，對人體而言就屬於無營養價值的膳食纖維，那麼為什麼還要食用菊糖呢？

菊糖有助於繁衍更多的有益菌

這是因為人體有益菌需要菊糖當作營養來源！有益菌可以分解、利用異果寡糖，作為其生長的營養來源，進而繁殖更多的有益菌，抑制壞菌的生長，維持腸道的健康環境。
再加上菊糖低熱量的特性，添加在幼童的營養補充品中，除了可以對腸胃道有所助益外，也可以避免因為攝取過多的蔗糖造成肥胖。
目前美國尚未制定菊糖與果寡糖類產品之每日容許攝取量(ADI)，一般每日之攝取量為1-4克，而歐洲國家則約3-11克。
在慢性毒性試驗中，研究人員長時間（104週）高劑量（2.17g/kg bw/day）給予動物攝取，並無發現對動物體生長發育或繁殖造成影響，也無致癌、致突變性及基因毒性，因此安全性極高。
不過，研究人員以提醒，人體過量攝取菊糖時(20g/day以上)，會引起腸胃脹氣等不適，故建議菊糖或果寡糖每日攝取量應在20公克以下，避免引起腸胃不適或腹瀉。.'''}
	return HttpResponse(json.dumps(data,ensure_ascii = False),content_type="application/json; charset=utf-8")












