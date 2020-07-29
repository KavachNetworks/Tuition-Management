from django import forms
from .models import Subject

class SubjectsAddForm(forms.ModelForm):
	class Meta:
		model=Subject()
		fields=['subject_code','subject_name','enrollment_name']