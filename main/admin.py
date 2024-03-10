from django.contrib import admin

from .models import  (
    AnswerQuestion,
    Category,
    Question
)

@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "question", "answer", "ball")    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author")    


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "correct_answer")    

