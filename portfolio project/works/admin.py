from django.contrib import admin
from .models import work

@admin.register(work)
class Workadmin(admin.ModelAdmin):
    list_display = ("Work_id","Title","Gitlink")