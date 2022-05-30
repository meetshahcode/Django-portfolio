
from django.db import models

class works(models.Model):
    #image
    image = models.ImageField(upload_to = 'images/')
    #id
    works_id = models.AutoField(primary_key=True)
    summary = models.TextField()
    