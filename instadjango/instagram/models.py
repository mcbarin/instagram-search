from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    access_token = models.CharField(max_length=100)
    insta_id = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)