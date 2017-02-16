from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import *

urlpatterns = [
url(r'^$', SaveDocument, name = 'home'),
url(r'index/', SaveDocument, name = 'SaveDocument'),
url(r'results/', TasksView, name = 'TasksView'),
url(r'^download/(?P<pk>\d+)/$', download, name = 'download')
]