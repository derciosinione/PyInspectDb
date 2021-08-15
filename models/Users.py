from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True, unique=False)
	name = models.CharField(max_length=100, blank=True, null=True, unique=False)
	email = models.CharField(max_length=100, blank=True, null=True, unique=False)
	age = models.IntegerField(blank=True)

	class Meta:
		db_table = 'Users'