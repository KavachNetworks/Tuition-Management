from django.contrib import admin

# Register your models here.
from .models import Subject,Staff,Student,Enrollment

from .forms import SubjectsAddForm,StaffsAddForm,StudentsAddForm,EnrollmentsAddForm

class EnrollmentCreateAdmin(admin.ModelAdmin):
	list_display=['enrollment_name','subject_code']
	form=EnrollmentsAddForm

class SubjectCreateAdmin(admin.ModelAdmin):
	list_display=['subject_code','subject_name']
	form=SubjectsAddForm
	search_fields=['subject_name']


class StaffCreateAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','staff_ph_no','addr','subject_code','staff_date_joined']
	form=StaffsAddForm
	list_filter=['subject_code']
	search_fields=['first_name','last_name']	


class StudentCreateAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','student_ph_no','addr','enrollment_name']
	form=StudentsAddForm
	search_fields=['first_name','last_name']

admin.site.register(Enrollment,EnrollmentCreateAdmin)
admin.site.register(Subject,SubjectCreateAdmin)
admin.site.register(Staff,StaffCreateAdmin)
admin.site.register(Student,StudentCreateAdmin)
