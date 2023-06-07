# models.py

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=255)
    question_type = models.IntegerField()
    order = models.IntegerField()
    text_area = models.BooleanField(default=False)


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.answer_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", blank=True, null=True)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text