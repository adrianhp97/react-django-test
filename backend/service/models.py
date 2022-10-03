from email.policy import default
from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    service_number = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
