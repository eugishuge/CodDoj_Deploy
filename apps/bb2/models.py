from __future__ import unicode_literals
from ..login.models import User
from datetime import datetime, date
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def quote(self, quote, session):
        error = []
        flag = True

        if len(quote['author'])<3:
            error.append("Please give credit to the quoter. Quoter name must be longer than 3 characters")
            flag = False

        if len(quote['quote'])<10:
            error.append("Please contribute a valid quote. Quotes must be longer than 10 characters")
            flag = False

        if flag:
            Quotes.objects.create(author = quote['author'],quote = quote['quote'], posted_by = session)
            return True
        else:
            return (False, error)

class Quotes(models.Model):
    user_id = models.ForeignKey(User)
    author = models.CharField(max_length = 255)
    quote = models.TextField(max_length = 1000)
    posted_by = models.CharField(max_length = 255)
    objects = UserManager()
    def __str__(self):
        return self.name

class Join(models.Model):
    all_users = models.ForeignKey(User, related_name="everyone")
    all_quotes = models.ForeignKey(Quotes, related_name="everything")
