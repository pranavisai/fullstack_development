from django.db import models

class User(models.Model):
    First_name = models.CharField(max_length=264)
    Last_name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=264, unique=True)

    
