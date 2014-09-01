from django.conf.urls import patterns, url

from fda import views

urlpatterns = patterns('',
        # ex: /polls/
        url(r'^$', views.index, name='index'),
        url(r'^genData/', views.genData, name='genData'),
		url(r'^showGraph/', views.showGraph, name='showGraph'),
		url(r'^getGraphData/', views.getGraphData, name='getGraphData'),

		url(r'^genData2', views.genData, name='genData'),
		url(r'^showGraph2/', views.showGraph2, name='showGraph2'),
		url(r'^getGraphData2', views.getGraphData2, name='getGraphData2'),

        # ex: /polls/5/
#         url(r'^(?P<poll_id>\d+)/$', views.detail,
#             name='detail'),
#         # ex: /polls/5/results/
#         url(r'^(?P<poll_id>\d+)/results/$',
#             views.results, name='results'),
#         # ex: /polls/5/vote/
#         url(r'^(?P<poll_id>\d+)/vote/$',
#             views.vote, name='vote'),
)
