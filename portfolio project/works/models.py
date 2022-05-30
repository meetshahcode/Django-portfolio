
from django.db import models

class work(models.Model):
    #image
    Image = models.ImageField(upload_to = 'images/',null = True,blank=True)
    #id
    Work_id = models.AutoField(primary_key=True)
    #title
    Title = models.CharField(max_length=100,blank=False,unique=True,null=False)
    #Detail
    Detail = models.TextField(null=True)
    #git link
    Gitlink = models.URLField(blank=True)
    #git boolean
    Gitbool = models.BooleanField(default=False,blank=False,null=False)
    #project website
    Livelink = models.URLField(blank=True)
    #project boolean
    Livebool = models.BooleanField(default=False,blank=False,null=False)

    def __str__(self):
        return self.Title

