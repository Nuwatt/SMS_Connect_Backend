from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .managers import CustomUserManager

class CustomUserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Personal info', {'fields': ('photo_file_name','nationality', 'country','city', 'date_of_birth', 'contact_number')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name', 'last_name', 'status', 'isDeleted', 'created', 'updated', 'photo_file_name','nationality', 'country','city', 'date_of_birth', 'contact_number'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
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