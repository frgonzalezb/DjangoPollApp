# Ref 1 (basic admin): https://docs.djangoproject.com/en/5.0/intro/tutorial02/
# Ref 2 (customization): https://docs.djangoproject.com/en/5.0/intro/tutorial07/
from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)


'''
# First customization

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question)
'''

'''
# Simple admin register Choice model
admin.site.register(Choice)
'''

