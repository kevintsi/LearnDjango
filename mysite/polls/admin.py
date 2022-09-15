from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# admin.site.register(Question)  # Models visible dans l'administrateur django


# Classe permettant d'ajouter directement plusieurs choix lors de la création d'une question
class ChoiceInline(admin.TabularInline):  # admin.TabularInLine et admin.StackedInLine
    model = Choice  # Model utilisé
    extra = 3  # Nombre minimal de choix


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # Choisir' l'ordre et les champs à afficher dans le formulaire admin
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ("question_text", "pub_date", "was_published_recently")

    list_filter = ["pub_date"]

    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
