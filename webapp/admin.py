from django.contrib import admin
from .models import record

class MyrecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')


# Register your models here.
admin.site.register(record,MyrecordAdmin)