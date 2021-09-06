from django.db import models


class Tag(models.Model):
    content = models.TextField(null=False, max_length=30, unique=True)

    def __str__(self):
        return self.content