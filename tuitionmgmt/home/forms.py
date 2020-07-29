from django import forms
from .models import Subject,Staff,Student

class SubjectsAddForm(forms.ModelForm):
	class Meta:
		model=Subject()
		fields=['subject_code','subject_name','enrollment_name']


class StaffsAddForm(forms.ModelForm):
	class Meta:
		model=Staff()
		fields=['first_name','last_name','staff_ph_no','addr','subject_code']		

class StudentsAddForm(forms.ModelForm):
	class Meta:
		model=Student()
		fields=['first_name','last_name','student_ph_no','addr']