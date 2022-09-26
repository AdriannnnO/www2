#import imp
from django.contrib import admin
#import django.contrib
from blog.models import Answer, Question,Choice
# models = django.apps.apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# class AuthorAdmin(admin.ModelAdmin):
#     pass

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ("question_text",)
    list_filter = ("question_text",'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice_text','votes')
    search_fields = ("choice_text",)
    list_filter = ("votes",)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','answer')
    search_fields = ('question','answer')
    list_filter = ('question',"answer")

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Answer,AnswerAdmin)