from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .models import Survey, Answer, Question
from .serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

class SurveyAPICreate(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def create(self, request, *args, **kwargs):
        survey_serializer = self.get_serializer(data=request.data)
        survey_serializer.is_valid(raise_exception=True)
        survey = survey_serializer.save()

        questions_data = request.data.pop('questions')
        for question_data in questions_data:
            choices_data = question_data.pop('choices')
            question_serializer = QuestionSerializer(data=question_data)
            question_serializer.is_valid(raise_exception=True)
            question = question_serializer.save(survey=survey)
            for choice_data in choices_data:
                choice_serializer = ChoiceSerializer(data=choice_data)
                choice_serializer.is_valid(raise_exception=True)
                choice_serializer.save(question=question)


        serializer = self.get_serializer(survey)
        return Response(serializer.data)
class SurveyAPIAnswer(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    def create(self, request, *args, **kwargs):
        answers_data = request.data.pop('answers')
        for answer in answers_data:
            answer_serializer = self.get_serializer(data=answer)
            answer_serializer.is_valid(raise_exception=True)
            answer_serializer.save(question=Question.objects.get(pk=answer['question']), answer_text=answer['answer_text'])
        return Response({"answers": answers_data})

class SurveyAPIGetSurvey(generics.RetrieveAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
