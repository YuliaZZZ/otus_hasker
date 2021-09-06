from django.conf import settings
from django.db import models

from .base import Base
from .tags import Tag


class Question(Base):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='question_author')
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name='question_rating')
    title = models.CharField(null=False, max_length=255)
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions', max_length=3)

    def __str__(self):
        return self.title
