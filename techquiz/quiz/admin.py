from django.contrib import admin

# Register your models here.
from .models import *

# Username (leave blank to use 'hp'): admin@sahil
# Email address: sahildhala123@gmail.com
# Password: 1234
# Password (again): 1234

# -----------------------------------`Separetly showing`--------------
# admin.site.register(Category)
# admin.site.register(Question)
# admin.site.register(Answer)



# ------------------------------------------`combine showing`--------------
admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)