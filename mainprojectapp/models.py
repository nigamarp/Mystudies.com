from datetime import timezone
from time import time
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Registration_no = models.CharField(max_length=100)
class comment(models.Model):
    user=models.CharField(max_length=100)
    content=models.TextField()
    time=models.DateTimeField(default=datetime.now, blank=True)

