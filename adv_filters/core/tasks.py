from __future__ import absolute_import
import time
from celery import shared_task, current_task
from .models import Document

@shared_task(name="cluster")
def cluster(param, job_id):
	c = Document.objects.get(id = job_id)
	c.task_status = "SUCCESS"
	c.save()
	return 'The test task executed with argument "%s" ' % param