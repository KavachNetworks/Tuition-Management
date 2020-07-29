from django.db import models

# Create your models here.
'''
class Staff(models.Model):
	fname=models.CharField(max_length=250)
	lname=models.CharField(max_length=250)
	staff_ph_no=models.CharField(max_length=10)
	address=models.TextField()
	staff_username=models.CharField(max_length=200)
	staff_password=models.CharField(max_length=200)

'''
class Subject(models.Model):
	subject_code=models.CharField(max_length=50,primary_key=True)
	subject_name=models.CharField(max_length=100)
	enrollment_name=models.CharField(max_length=50)

	def __str__(self):
		return self.subject_name