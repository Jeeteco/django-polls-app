from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class Choiceinline(admin.TabularInline):
    model =Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{
            "fields":['Question_text']
        }),
        ('Date information',{"fields":['pub_date'], 'classes':['collapse']})
        
    ]
    
    inlines=[Choiceinline]
    list_display=('question_text','pub_date')
    list_filter=('pub_date')
    search_fields=['quetion_text']
    
admin.site.register(Choice)
admin.site.register(Question)
