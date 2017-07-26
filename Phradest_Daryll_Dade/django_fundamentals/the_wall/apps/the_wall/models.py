from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string = "name: {}, email {}, password {}, created_at {}, updated_at {},"

        assert False
        return string.format(
            self.name,
            self.email,
            self.password,
        )

class Post(models.Model):
    post = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
