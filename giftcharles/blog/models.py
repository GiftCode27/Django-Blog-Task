from django.db import models
from django.contrib.auth.import user model
from datetime import datetime
from django.utils.timezone import timezone

# Create your models here.

Class Post(models.model):
Title = models.CharField(max_Length=200)
Text = models.TextField(max_Length=200)
Author = models.ForeignKeys(get_user_model(), on_delete=models.CASCADE)
Created_date = models.DateTimeField(auto_now=True)
Published_date = models.DateTimeField(auto_now=True)





