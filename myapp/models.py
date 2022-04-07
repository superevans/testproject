from email.policy import default
from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100, default="Default Name")
    details = models.CharField(max_length=500, default="Default Details")


#old Feature class
# class Feature:
#     id: int
#     name: str
#     details: str
#     is_true: bool