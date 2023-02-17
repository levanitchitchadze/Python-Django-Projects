from django.db import models
import datetime



# registration model
# რეგისტრაციის მოდელი 
class Customers(models.Model):
  username = models.CharField(max_length=255)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Email = models.CharField(max_length=255)
  MobileNumber = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  BirthDate = models.DateField("BirthDate")
  CreateDate = models.DateField("CreateDate", default=datetime.date.today)
  Gender = models.CharField(max_length=20)

class Contact(models.Model):
  Name=models.CharField(max_length=255)
  Email=models.CharField(max_length=255)
  Message=models.TextField()

class AboutModel(models.Model):
  Text=models.TextField()