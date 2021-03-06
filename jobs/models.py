from django.db import models

class Company(models.Model):
	company_name = models.CharField(max_length=900)
	company_description = models.CharField(max_length=3000)
	company_date_added = models.DateTimeField('date added')
	def __unicode__(self):
		return self.company_name

class District(models.Model):
	district_name = models.CharField(max_length=500)
	def __unicode__(self):
		return self.district_name

class Position(models.Model):
	position_name = models.CharField(max_length=600)
	position_description = models.CharField(max_length=3000)
	def __unicode__(self):
		return self.position_name

class Gender(models.Model):
	gender_description = models.CharField(max_length=20)
	def __str__(self):
		return self.gender_description

class Salary(models.Model):
	salary_district = models.ForeignKey(District)
	salary_position = models.ForeignKey(Position)
	salary_company = models.ForeignKey(Company)
	salary_gender = models.ForeignKey(Gender)
	salary_value = models.IntegerField(default=0)
	salary_ip = models.CharField(max_length=100)
	salary_date = models.DateTimeField('date published')
	def __int__(self):
		return self.salary_value
