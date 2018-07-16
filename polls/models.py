from django.db import models
from django.utils import timezone       #for timezone
import datetime                         #for date and time

#creates a polling model


class Question(models.Model):                                   #class for adding questions
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #to make returning convienient to read: 

    def __str__(self):              
        return self.question_text


class Choice(models.Model):                                             #class for adding options
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #to make returning convienient to read: 

    def __str__(self):
        return self.choice_text

# Create your models here.
