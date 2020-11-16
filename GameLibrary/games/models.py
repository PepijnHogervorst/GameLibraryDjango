from django.db import models

from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    # Properties
    name = models.CharField(max_length=200)
    description = models.TextField()
    materials = models.TextField()
    duration_min = models.IntegerField()
    duration_max = models.IntegerField()
    group_size_min = models.IntegerField()
    group_size_max = models.IntegerField()
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # To string method
    def __str__(self):
        return self.name




