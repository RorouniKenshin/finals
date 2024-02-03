from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    
    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    last_name = models.CharField(max_length=55, null=True)
    first_name = models.CharField(max_length=55, null=True)
    middle_name = models.CharField(max_length=55, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=1, choices=genderChoices)
    address = models.CharField(max_length=55, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.last_name
    
    

class Schedule(models.Model):
    name = models.CharField(max_length=55, null=True)
    date = models.DateTimeField(null=True)
    email = models.CharField(max_length=55, null=True)
    total_person = models.PositiveIntegerField(null=True)
    total_cottage = models.PositiveIntegerField(null=True)
    message = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
class Payment(models.Model):
    image = models.ImageField(upload_to="payment", null=True)
    amount = models.PositiveIntegerField(null=True)
    ref_number = models.PositiveIntegerField(null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.ref_number
    
class News(models.Model):
    title = models.CharField(max_length=55, null=True)
    content = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

class Event(models.Model):
    image = models.ImageField(upload_to="events", null=True)
    name = models.CharField(max_length=55, null=True)
    description = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=55, null=True)
    image = models.ImageField(upload_to="gallery", null=True)
    description = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name