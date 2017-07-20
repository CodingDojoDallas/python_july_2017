from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# def __str__(self):
 #    	return self.first_name + " " + self.last_name

class Post(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	# Notice the association made with ForeignKey for a one-to-many relationship
		# There can be many posts to one User
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
	title = models.CharField(max_length=100)
	blog = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
  
class Comment(models.Model):
	blog = models.ForeignKey(Blog)
	comment = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)