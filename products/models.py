from django.db import models

# todo/todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    category = models.CharField(max_length = 150)
    description = models.CharField(max_length = 1000)
    manufacture = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)


    def __str__(self):
        return self.name