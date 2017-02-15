from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    doc = models.FileField(upload_to='input_files')
    status = models.CharField(max_length = 100, blank = True)
    task_id = models.CharField(max_length = 100, blank = True)
    task_status = models.CharField(max_length = 100)
    input_file_path = models.CharField(max_length = 100, blank = True)
    output_file_path = models.CharField(max_length = 100, blank=True)
    name = models.CharField(max_length = 100, blank=True)

