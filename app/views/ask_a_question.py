from django.contrib.auth import get_user
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import mixins, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.forms.question import QuestionForm
from app.models.questions import Question
from app.serializers.question import QuestionSerializer


class AskQuestionView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet
                      ):
    model = Question
    template_name = "ask_a_question.html"
    serializer_class = QuestionSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        user = get_user(request)
        form = QuestionForm()
        return Response({'form': form, 'user': user})

    def create(self, request, *args, **kwargs):
        user = get_user(request)
        form = QuestionForm(data=request.data)
        if form.is_valid():
            serializer = QuestionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=user)
        else:
            return HttpResponse(form.errors)
        return redirect('/ask')

