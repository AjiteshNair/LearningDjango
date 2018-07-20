from django.db import models
from django.utils import timezone       #for timezone
import datetime                         #for date and time

#creates a polling model


class Question(models.Model):                                   #class for adding questions
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
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
