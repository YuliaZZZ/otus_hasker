from rest_framework import serializers

from app.models.answers import Answer
from app.models.questions import Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("author", "content", "votes", "question", "created_date",)