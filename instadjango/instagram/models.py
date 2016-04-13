from django.contrib.postgres.fields import ArrayField
from django.db import models


class Photo(models.Model):
    username = models.CharField(max_length=50)
    profile_picture = models.URLField(max_length=250)
    full_name = models.CharField(max_length=100)
    picture_url = models.URLField(max_length=250)
    post_id = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=50), blank=True)


class HashTag(models.Model):
    hashtag = models.CharField(max_length=50)
    search_count = models.IntegerField(default=1)
    related_tags = ArrayField(models.CharField(max_length=50), blank=True)

    def increment_counter(self):
        self.search_count += 1
        self.save()
