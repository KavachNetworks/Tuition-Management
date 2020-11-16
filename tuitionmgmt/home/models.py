from django.db import models
from django.utils import timezone
# Create your models here.

class Subject(models.Model):
	subject_code=models.CharField(max_length=50,primary_key=True)
	subject_name=models.CharField(max_length=100)

	def __str__(self):
		return self.subject_code

class Enrollment(models.Model):
	enrollment_name=models.CharField(max_length=50,primary_key=True)
	subject_code=models.ForeignKey(Subject,on_delete=models.CASCADE)

	def __str__(self):
		return self.enrollment_name

class Staff(models.Model):
	first_name=models.CharField(max_length=250)
	last_name=models.CharField(max_length=250)
	staff_ph_no=models.CharField(max_length=10)
	addr=models.TextField()
	staff_username=models.CharField(max_length=200,blank=True)
	staff_password=models.CharField(max_length=200,blank=True)
	subject_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
	staff_date_joined=models.DateField(default=timezone.now())

	def __str__(self):
		return self.first_name+' '+self.last_name

class Student(models.Model):
	DEFAULT_VALUE="CSE"
	first_name=models.CharField(max_length=250)
	last_name=models.CharField(max_length=250)
	student_ph_no=models.CharField(max_length=10)
	addr=models.TextField()
	student_uname=models.CharField(max_length=200,blank=True)
	student_password=models.CharField(max_length=200,blank=True)
	enrollment_name=models.ForeignKey(Enrollment,on_delete=models.CASCADE,default=DEFAULT_VALUE)

	def __str__(self):
		return self.first_name+' '+self.last_name


		