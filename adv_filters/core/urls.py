from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import *

urlpatterns = [
url(r'^$', TemplateView.as_view(
	template_name = 'index.html'), name = 'home'),
url(r'saved/', SaveDocument, name = 'SaveDocument'),
url(r'results/', TasksView, name = 'TasksView'),
url(r'^download/(?P<pk>\d+)/$', download, name = 'download')
]