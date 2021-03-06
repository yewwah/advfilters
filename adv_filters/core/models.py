from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    doc = models.FileField(upload_to='cars')
    status = models.CharField(max_length = 100)
    task_id = models.BigIntegerField()
    input_file_path = models.CharField(max_length = 100)
    output_file_path = models.CharField(max_length = 100, blank=True)
