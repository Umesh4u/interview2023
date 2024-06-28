from django.db import models

# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=100)
	mobile = models.CharField(max_length=10)
	address = models.TextField(max_length=200,blank=True)

	def __str__(self):
		return self.name

		
