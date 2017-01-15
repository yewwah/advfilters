from django.shortcuts import render, redirect

# Create your views here.
from forms import DocumentForm
from models import Document
from django.apps import apps
from .tasks import test2
myapp = apps.get_app_config('django_celery_results')
TASK_MODEL = myapp.models['taskresult']

def tasks_view(request):
    tasks = TASK_MODEL.objects.all()

    lst = []
    for task in tasks:
        item = Document.objects.filter(task_id = task.task_id)
        for c in item:
            c.status = task.status
            print c.output_file_path
            c.save()
            lst.append(c)
    return render(request, 'saved.html', {'tasks': lst})

def SaveDocument(request):
    saved = False
    if request.method == "POST":
        #Get the posted form
        MyDocumentForm = DocumentForm(request.POST, request.FILES)
                
        if MyDocumentForm.is_valid():
            document = Document()
            document.name = MyDocumentForm.cleaned_data["name"]
            document.doc = request.FILES["document"]
            task = test2.delay(document.name, document.id)
            document.status = task.status
            document.task_id = task.task_id
            document.input_file_path = 'input_files/' + document.doc.name
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
    return redirect('home')
    