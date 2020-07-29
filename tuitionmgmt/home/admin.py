from django.contrib import admin

# Register your models here.
from .models import Subject,Staff

from .forms import SubjectsAddForm,StaffsAddForm



class SubjectCreateAdmin(admin.ModelAdmin):
	list_display=['subject_code','subject_name','enrollment_name']
	form=SubjectsAddForm
	list_filter=['enrollment_name']
	search_fields=['subject_name','enrollment_name']


class StaffCreateAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','staff_ph_no','addr','subject_code','staff_date_joined']
	form=StaffsAddForm
	list_filter=['subject_code']
	search_fields=['first_name','last_name']	

admin.site.register(Subject,SubjectCreateAdmin)
admin.site.register(Staff,StaffCreateAdmin)