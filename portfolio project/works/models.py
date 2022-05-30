
from django.db import models

class work(models.Model):
    #image
    image = models.ImageField(upload_to = 'images/')
    #id
    work_id = models.AutoField(primary_key=True)
    #summary
    summary = models.TextField()
