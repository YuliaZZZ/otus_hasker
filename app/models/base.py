from datetime import timedelta, datetime

from django.db import models
from django.utils import timezone


class Base(models.Model):
    content = models.TextField(null=False, max_length=255)
    rating = models.IntegerField(default=0, db_index=True)
    created_date = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        abstract = True

    # def summary_rating(self):
    #     self.rating = len(self.votes)
