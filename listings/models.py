from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
   realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
   title = models.CharField(max_length=200)
   address = models.CharField(max_length=200)
   address_2 = models.CharField(max_length=200)
   city = models.CharField(max_length=100)
   state = models.CharField(max_length=100)
   zipcode = models.CharField(max_length=20)
   longitude_latitude = models.CharField(max_length=200)
   year_built = models.IntegerField()
   minimum_age = models.IntegerField()
   community_description = models.TextField(blank=True)
   studio_price = models.IntegerField()
   one_bedroom_price = models.IntegerField()
   two_bedrooms_price = models.IntegerField()
   private_price = models.IntegerField()
   semi_private_price = models.IntegerField()
   meals = models.BooleanField(default=False)
   pets = models.BooleanField(default=False)
   resident_parking = models.BooleanField(default=False)
   photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
   photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   is_published = models.BooleanField(default=True)
   list_date = models.DateTimeField(default=datetime.now, blank=True)
   def __str__(self):
     return self.title