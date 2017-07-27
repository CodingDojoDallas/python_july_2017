from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class BookManager(models.Manager):
    def validateReview(self, form_data):
        errors = []

        if len(form_data['content']) == 0:
            errors.append("Review content is required.")
        if len(form_data['rating']) == 0:
            errors.append("Review rating is required.")

        return errors

    def addBook(self, form_data, user):
        book = Book.objects.create(
            title = form_data['title'],
            author = form_data['author'],
            review = form_data['content'],
            rating = form_data['rating'],
            user = user
        )
        return book


class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        errors = []

        if len(form_data['first_name']) == 0:
            errors.append("First name is required")

        # first name must be letters only
        if form_data['first_name'].isalpha() == False:
            errors.append("Invalid first name")

        if len(form_data['last_name']) == 0:
            errors.append("Last name is required")

        # last name must be letters only
        if form_data['last_name'].isalpha() == False:
            errors.append("Invalid last name")

        if len(form_data['email']) == 0:
            errors.append("Email is required")

        # email must be in valid format
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Invalid email address")

        if len(form_data['password']) == 0:
            errors.append("Password is required")

        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords do not match")

        return errors

    def createUser(self, form_data):
        password = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = hashed_pw
        )

        return user

    def validateLogin(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append("Email is required")

        if len(form_data['password']) == 0:
            errors.append("Password is required")

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    review = models.TextField(max_length=1000)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    user = models.ForeignKey(User, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()
