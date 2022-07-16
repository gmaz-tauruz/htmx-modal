from django.db import models
from django.db.models.functions import Lower


class Employee(models.Model):

    GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
    ]
    
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.last_name} , {self.first_name} {self.middle_name}"
        