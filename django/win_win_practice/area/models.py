from django.db import models
from configuration.models import Common

# Create your models here.
class Area(Common):
	name = models.CharField(max_length=100, unique=True,verbose_name="Area Name")
	priority=models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return self.name


class State(Common):
	name = models.CharField(max_length=100,unique=True,verbose_name="State Name")
	area = models.ForeignKey(Area, related_name="Area_area", on_delete=models.CASCADE,null=True, limit_choices_to={'active_status':'1'})

	def __str__(self):
		return self.name

class City(Common):
	name = models.CharField(max_length=100,unique=True,verbose_name="City Name")
	state = models.ForeignKey(State, related_name="State_state", on_delete=models.CASCADE,null=True, limit_choices_to={'active_status':"1"})

	def __str__(self):
		return self.name

