from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import *

urlpatterns = [
url(r'^$', TemplateView.as_view(
	template_name = 'profile.html'), name = 'home'),
url(r'saved/', SaveDocument, name = 'SaveDocument'),
url(r'check/', tasks_view, name = 'tasks_view'),
url(r'^test/(?P<pk>\d+)/$', test, name = 'test')
]