from django.db import DatabaseError
from itertools import islice

from rest_framework import serializers

from app.models.questions import Question
from app.models.tags import Tag
from app.serializers.answers import AnswerSerializer
from app.serializers.tags import TagSerializer
from app.serializers.users import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    answers = AnswerSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ("author", "title", "tags", "votes", "answers", "created_date",)

    @property
    def validated_data(self):
        tags_list = self.initial_data['tags'].replace(', ', ',')
        tags_list = self.initial_data['tags'].split(',')[:3]
        tags_new = [tag for tag in tags_list if tag not in [c.content for c in Tag.objects.all()]]
        batch = list(islice((Tag(content=i) for i in tags_new), len(tags_new)))
        try:
            Tag.objects.bulk_create(batch, len(tags_new))
        except DatabaseError:
            pass
        tags = Tag.objects.filter(content__in=tags_list).all()
        new_data = self.initial_data.copy()
        new_data["tags"] = tags
        new_data.pop("csrfmiddlewaretoken")
        return new_data
