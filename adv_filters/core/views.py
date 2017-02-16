from django.shortcuts import render, redirect

# Create your views here.
from forms import DocumentForm
from models import Document
from django.http import HttpResponse
from .tasks import cluster
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str
import os

def TasksView(request):
    item = Document.objects.all()
    return render(request, 'results.html', {'tasks': item})

def SaveDocument(request):
    if request.method == "POST":
        # Get the posted form
        MyDocumentForm = DocumentForm(request.POST, request.FILES)
        if MyDocumentForm.is_valid():
            document = Document()
            document.name = MyDocumentForm.cleaned_data["name"]
            document.doc = request.FILES["document"]
            document.task_status = "PENDING"
            document.input_file_path = 'input_files/' + document.doc.name
            document.output_file_path = 'input_files/' + document.doc.name
            document.save()
            task = cluster.delay(document.name, document.id)
            return redirect('TasksView')
        else:
            return render(request, 'index.html', {'form': MyDocumentForm})
    else:
        MyDocumentForm = DocumentForm()
        return render(request, 'index.html', {'form': MyDocumentForm})
    return render(request, 'results.html')


def download(request, pk):
    print 'inside request'
    course = Document.objects.get(pk=pk)
    path_to_file = os.getcwd() + os.sep + course.output_file_path
    file_name = path_to_file
    print 'path to file', path_to_file
    wrapper = FileWrapper(file(path_to_file))
    response = HttpResponse(wrapper, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response
