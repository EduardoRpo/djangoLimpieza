from operator import mod
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Tipo)

class DocumentosAdmin(admin.ModelAdmin):
    list_display=['fecha','tipo','image','observaciones']
    search_fields=["observaciones"]
    list_filter=['fecha','tipo__nombre']



admin.site.register(Documentos, DocumentosAdmin)