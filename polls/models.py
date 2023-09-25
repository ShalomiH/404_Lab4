from django.db import models

# Create your models here

# Question and Choice entities, with subfields.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# Choice has ForeignKey, each Choice belongs to a Question, will be deleted if
# deleted if the Parent is (on_delete)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)