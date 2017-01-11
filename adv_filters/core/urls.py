from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import *

urlpatterns = [
url(r'^$', TemplateView.as_view(
	template_name = 'profile.html')),
url(r'profile/',TemplateView.as_view(
      template_name = 'profile.html')), 
url(r'saved/', SaveDocument, name = 'SaveDocument'),
url(r'check/', tasks_view, name = 'tasks_view')
]