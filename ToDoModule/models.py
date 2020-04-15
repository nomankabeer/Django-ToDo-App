from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class ToDoModule(models.Model):
    text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.text