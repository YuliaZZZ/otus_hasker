from django.conf import settings
from django.db import models

from .base import Base
from .questions import Question


class Answer(Base):
    question = models.ForeignKey(Question, on_delete=models.PROTECT,
                                 related_name='answer_of_question',
                                 default=None, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='answer_author')
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name='answer_rating')
    flag = models.BooleanField(default=None, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'author'], name='answers version')]

    def __str__(self):
        return self.author
