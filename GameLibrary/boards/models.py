import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    # Properties
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # To string method
    def __str__(self):
        return self.question_text

    # Custom method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Properties
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # To string method
    def __str__(self):
        return self.choice_text
