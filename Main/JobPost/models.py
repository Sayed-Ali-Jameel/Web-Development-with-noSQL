
# Create your models here.
from djongo import models
from djongo.models import Model
from django.contrib.auth.models import User


# Create your models here.
class Post(Model):
    title         = models.CharField(max_length=255)
    posted_by     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    description   = models.TextField()
    responsibility = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    created_on    = models.DateTimeField(auto_now_add=True)
    applicants = models.ManyToManyField(User,blank=True)


