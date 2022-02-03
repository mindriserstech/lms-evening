from pyexpat import model
from django.db import models

# Create your models here.
class UserType(models.Model):
    user_type = models.CharField(max_length=100)

    class Meta:
        db_table = "lms_usertype"

# user model
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "lms_users"