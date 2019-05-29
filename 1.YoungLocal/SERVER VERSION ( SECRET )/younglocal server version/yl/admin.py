from django.contrib import admin

# Register your models here.
# Register your models here.
# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.utils import text
from django import forms
from .models import CustomUser, Category, Article, Comment

#class CustomArticleAdmin(admin.ModelAdmin):
  #  add_form = CustomArticleCreationForm
    #form = CustomUserChangeForm
   # model = Article
    #list_display = [field.name for field in Article._meta.fields if field.name != "id"]
    
    #def get_form(self, request, obj=None, **kwargs):
     #   username = request.user.get_username()
      #  form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
       # form.base_fields['article_author'].initial = username
        #return form




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [field.name for field in CustomUser._meta.fields if field.name != "id"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)