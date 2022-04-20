from django.db import models

# Create your models here.

class BuildingGroup(models.Model):
	grp_name  =  models.CharField(max_length=40)
	grp_description = models.TextField(max_length=400)
	is_status = models.BooleanField(default=True)
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.grp_name


class BuildingDetails(models.Model):
	build_name = models.CharField(max_length=40)
	build_address = models.TextField(max_length=400)
	building_grp = models.ForeignKey(BuildingGroup,on_delete=models.CASCADE,related_name='constructedby')
	region = models.CharField(max_length=40)
	country = models.CharField(max_length=40)
	point_of_contact = models.CharField(max_length=40)
	email = models.EmailField()
	contact = models.CharField(max_length=40)
	is_status = models.BooleanField(default=True)
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.build_name

