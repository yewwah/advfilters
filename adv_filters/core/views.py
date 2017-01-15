from django.shortcuts import render, redirect

# Create your views here.
from forms import DocumentForm
from models import Document
from django.apps import apps
from django.http import HttpResponse
from .tasks import test2
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str
import os
myapp = apps.get_app_config('django_celery_results')
TASK_MODEL = myapp.models['taskresult']


def tasks_view(request):
    tasks = TASK_MODEL.objects.all()

    lst = []
    for task in tasks:
        item = Document.objects.filter(task_id=task.task_id)
        for c in item:
            c.status = task.status
            print c.output_file_path
            c.save()
            lst.append(c)
    return render(request, 'saved.html', {'tasks': lst})


def SaveDocument(request):
    saved = False
    if request.method == "POST":
        # Get the posted form
        print 'Uploading File'
        MyDocumentForm = DocumentForm(request.POST, request.FILES)

        if MyDocumentForm.is_valid():
            document = Document()
            document.name = MyDocumentForm.cleaned_data["name"]
            document.doc = request.FILES["document"]
            task = test2.delay(document.name, document.id)
            document.status = task.status
            document.task_id = task.task_id
            document.input_file_path = 'input_files/' + document.doc.name
            print document.input_file_path
            document.output_file_path = 'input_files/' + document.doc.name
            document.save()
            return redirect('tasks_view')
        else:
            print 'Fails'
    else:
        MyDocumentForm = DocumentForm()

    return render(request, 'saved.html', locals())


def test(request, pk):
    print 'inside request'
    course = Document.objects.get(pk=pk)
    path_to_file = os.getcwd() + os.sep + course.output_file_path
    #/Users/macbookpro/Desktop/advfilters/adv_filters/input_files
    #/Users/macbookpro/Desktop/advfilters/adv_filters/input_files
    #/Users/macbookpro/Desktop/advfilters/adv_filters/input_files/pycon notes.rtf
    file_name = path_to_file
    print 'path to file', path_to_file
    wrapper = FileWrapper(file(path_to_file))
    response = HttpResponse(wrapper, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    #response['X-File'] = path_to_file
    return response
