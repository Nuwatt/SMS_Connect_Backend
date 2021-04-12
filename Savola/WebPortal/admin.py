from django.contrib import admin

from .models import *


admin.site.register(User)
admin.site.register(Roles)
admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Sku)
admin.site.register(QuestionnaireType)
admin.site.register(Questions)
# admin.site.register(Questionnaires)
admin.site.register(QuestionOptions)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Areas)
admin.site.register(Retailers)
admin.site.register(Stores)
admin.site.register(Surveys)
admin.site.register(SurveyActivities)
admin.site.register(Answers)