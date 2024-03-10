from django.db import models
from django.contrib.auth.models import User

from .enums import AnswerWord


class CustomModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Category(CustomModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return self.name

class Question(CustomModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    body = models.TextField()
    answers = models.JSONField()
    correct_answer = models.CharField(max_length = 1, choices = AnswerWord.get_choices())

    def __str__(self) -> str:
        return f"{self.author.get_full_name()} {self.title}"
    
class AnswerQuestion(CustomModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 1, choices = AnswerWord.get_choices())
    
    @property
    def ball(self):
        return self.question.correct_answer == self.answer

    def __str__(self) -> str:
        return f"{self.user.username} | {self.ball}"



