from django.db import models


# Create your models here.
class Game(models.Model):
    # Properties
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_min = models.IntegerField()
    duration_max = models.IntegerField()
    group_size_min = models.IntegerField()
    group_size_max = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    # To string method
    def __str__(self):
        return self.name

