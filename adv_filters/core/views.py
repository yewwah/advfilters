from django.shortcuts import render, redirect

# Create your views here.
from forms import DocumentForm
from models import Document
from django.apps import apps
from .tasks import test2
myapp = apps.get_app_config('django_celery_results')
TASK_MODEL = myapp.models['taskresult']

def tasks_view(request):
    print 'tasks'
    tasks = TASK_MODEL.objects.all()
    print 'in tasks view'
    print tasks[0]
    print tasks[0].status
    return render(request, 'saved.html', {'tasks': tasks})

def SaveDocument(request):
    saved = False
    if request.method == "POST":
        #Get the posted form
        MyDocumentForm = DocumentForm(request.POST, request.FILES)
                
        if MyDocumentForm.is_valid():
            document = Document()
            document.name = MyDocumentForm.cleaned_data["name"]
            document.doc = request.FILES["document"]
            try:
                document.save()
            
                test2.delay(document.name)
            except:
                import traceback; traceback.print_exc()
            print 'completed celery tasks'
            saved = True

            return redirect('tasks_view')
        else:
            print 'Fails'
    else:
        MyDocumentForm = DocumentForm()

    return render(request, 'saved.html', locals())