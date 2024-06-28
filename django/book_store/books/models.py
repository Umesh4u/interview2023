from django.db import models
from configuration.models import BasicFields

# Create your models here.

class Author(BasicFields):
	name = models.CharField(max_length=100)

	class Meta:
		def __str__(self):
			return self.name

class Book(BasicFields):
	title = models.CharField(max_length=100)
	publication_date = models.DateField()
	price = models.PositiveIntegerField()
	author = models.OneToOneField(Author, on_delete=models.CASCADE)

	class Meta:
		def __str__(self):
			return self.title



class Store(BasicFields):
	name = models.CharField(max_length=100)
	address = models.TextField(max_length=200,null=True,blank=True)
	book = models.ManyToManyField(Book)

	class Meta:
		def __str__(self):
			return self.name
