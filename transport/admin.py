from django.contrib import admin

from . import models

admin.site.register(models.Agency)
admin.site.register(models.Calendar)
admin.site.register(models.CalendarDate)
admin.site.register(models.Department)
admin.site.register(models.Route)
admin.site.register(models.Stop)
admin.site.register(models.StopTime)
admin.site.register(models.Trip)
