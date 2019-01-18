from django.db import models

# Create your models here.

class ChatInfo(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=2000)
    category = models.CharField(max_length=100)

    # Returns answer for the particular model object
    def __str__(self):
        return self.answer
