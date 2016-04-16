from django.contrib.postgres.fields import ArrayField
from django.db import models


class Photo(models.Model):
    username = models.CharField(max_length=50)
    profile_picture = models.URLField(max_length=250)
    full_name = models.CharField(max_length=100)
    picture_url = models.URLField(max_length=250)
    post_id = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=50), blank=True)

class RelatedTag(models.Model):
    count = models.IntegerField(default=1)
    tag = models.CharField(max_length=50)
    related_hashtag = models.ForeignKey('instagram.HashTag', related_name='related_tag', null=True)
    def increment_counter(self):
        self.count += 1
        self.save()

class HashTag(models.Model):
    hashtag = models.CharField(max_length=50)
    search_count = models.IntegerField(default=1)

    def increment_counter(self):
        self.search_count += 1
        self.save()

    def add_related_tags(self, tags):
        for tag in tags:
            # check if contains

            if self.related_tag.filter(tag=tag).exists():
                obj = self.related_tag.get(tag=tag)
                obj.increment_counter()
            else:
                obj = RelatedTag.objects.create(tag=tag)
                obj.related_hashtag = self
                obj.save()



