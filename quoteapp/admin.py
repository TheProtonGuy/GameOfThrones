from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class ActorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(models.Actor, ActorAdmin)

class QuoteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(models.Quote, QuoteAdmin)