from django.db import models
from django.urls import reverse

# we are trying to mimic a school model

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.DO_NOTHING) 
    #this related name students is being used in the student-detail.html file

    def __str__(self):
        return self.name