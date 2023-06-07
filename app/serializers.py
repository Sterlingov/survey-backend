from django.forms import model_to_dict
from rest_framework import serializers
from .models import Survey, Question, Answer, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'order', "text_area","choices"]


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'created_at', 'questions']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text']


