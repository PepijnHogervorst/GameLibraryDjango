from django.db import models


# Create your models here.
class Question(models.Model):
    # Properties
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

    # To string method
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)