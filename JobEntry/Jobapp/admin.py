from django.contrib import admin
from .models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('id','cat','title', 'company', 'location', 'published_at', 'deadline','is_active')
    list_filter = ('cat','company', 'location', 'published_at','is_active')
    search_fields = ('cat','title', 'company', 'description', 'requirements')
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)

admin.site.register(Job, JobAdmin)
