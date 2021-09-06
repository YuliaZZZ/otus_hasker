from django.contrib.auth import get_user
from django.core.paginator import Paginator
from django.db.models import Count
from django.utils.timezone import now

from rest_framework import mixins, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.models.questions import Question
from app.serializers.question import QuestionSerializer


class IndexView(mixins.ListModelMixin,
                viewsets.GenericViewSet
                ):
    model = Question
    template_name = "index.html"
    serializer_class = QuestionSerializer
    parser_classes = (JSONParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [TemplateHTMLRenderer]

    queryset = Question.objects.all().order_by('-created_date')

    def list(self, request):
        user = get_user(request)

        hot_questions = Question.objects.all().order_by('-rating', '-created_date')
        q = hot_questions.annotate(votes_count=Count('votes'))
        trending = q.order_by('-votes_count')[:10]

        paginator = Paginator(self.queryset, 20)
        hot_paginator = Paginator(trending, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        hot_page_obj = hot_paginator.get_page(page_number)
        return Response({'questions': self.queryset, 'trending': trending,
                         'hot_questions': hot_questions, 'page_obj': page_obj,
                         'from_date': now(), 'hot_page_obj': hot_page_obj, 'user': user})
