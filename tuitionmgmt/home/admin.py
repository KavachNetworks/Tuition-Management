from django.contrib import admin

# Register your models here.
from .models import Subject,Staff,Student

from .forms import SubjectsAddForm,StaffsAddForm,StudentsAddForm



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



class StudentCreateAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','student_ph_no','addr']
	form=StudentsAddForm
	search_fields=['first_name','last_name']

admin.site.register(Subject,SubjectCreateAdmin)
admin.site.register(Staff,StaffCreateAdmin)
admin.site.register(Student,StudentCreateAdmin)
