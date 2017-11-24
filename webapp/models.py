from django.db import models

class employees(models.Model):
	firstname=models.CharField(max_length=10)
	lastname=models.CharField(max_length=10)
	emp_id=models.IntegerField()

	def _str_(self):
		return self.firstname
