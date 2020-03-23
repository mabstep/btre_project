from django.db import models
from datetime import datetime


class Realtor(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_admin = models.BooleanField(default=True)
  create_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name
  