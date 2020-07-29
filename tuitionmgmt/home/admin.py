from django.contrib import admin

# Register your models here.
from .models import Subject

from .forms import SubjectsAddForm



class SubjectCreateAdmin(admin.ModelAdmin):
	list_display=['subject_code','subject_name','enrollment_name']
	form=SubjectsAddForm
	list_filter=['enrollment_name']
	search_fields=['subject_name','enrollment_name']

admin.site.register(Subject,SubjectCreateAdmin)