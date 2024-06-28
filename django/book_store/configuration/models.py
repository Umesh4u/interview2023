from django.db import models

# Create your models here.
class BasicFields(models.Model):
	status = models.BooleanField(default=True)

	class Meta:
		abstract=True
