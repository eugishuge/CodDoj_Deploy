from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, login):

        error = []
        flag = True

        if len(login['email'])<1:
            error.append('you must enter a valid email')
            flag = False

        if not User.objects.filter(email = login['email']):
            error.append('Please register an account first')
            flag = False

        if not EMAIL_REGEX.match(login['email']):
            error.append("please enter your email in a valid format")
            flag = False

        if len(login['password'])<1:
            error.append('you must enter a valid password')
            flag = False

        if not User.objects.filter(password = login['password']):
            error.append('your password does not match your email')
            flag = False

        if flag:
            return True
        else:
            return (False, error)
######################################################################
    def register(self, register):
        error = []
        flag = True

        if len(register['name'])<1:
            error.append('you must enter a valid first name')
            flag = False

        if len(register['alias'])<1:
            error.append('you must enter a valid alias')
            flag = False

        if len(register['email'])<2:
            error.append('you must enter a valid email')
            flag = False

        if not EMAIL_REGEX.match(register['email']):
            error.append("please enter your email in a valid format")
            flag = False

        if User.objects.filter(email = register['email']):
            error.append('you have already registered')
            flag = False

        if len(register['password'])<8:
            error.append("your password must be at least 8 characters long")
            flag = False

        if register['confirm_pw'] != register['password']:
            error.append('your passwords do not match, please try again')
            flag = False

        if len(register['birthday']) < 1:
            error.append('please enter your birthday')
            flag = False

        birthday = datetime.strptime(register['birthday'],'%Y-%m-%d')
        now = datetime.today()

        if birthday > now:
            error.append('you must be born already to register')
            flag = False

        if flag:
            User.objects.create(name=register['name'], alias = register['alias'], email = register['email'], password = register['password'], birthday = register['birthday'])
            return True
        else:
            return (False, error)

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthday = models.DateField(blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    objects = UserManager()
    def __str__(self):
        return self.name
