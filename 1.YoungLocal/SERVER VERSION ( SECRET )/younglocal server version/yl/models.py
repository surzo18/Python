from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class CustomUser(AbstractUser):
    # add additional fields in here
    rights = models.CharField(default='reader', max_length=10)
    karma = models.IntegerField(default = 0 )
    about = models.CharField(max_length=1000, null=False)
    avatar = models.ImageField(upload_to = 'static/other/avatar/', default='static/other/avatar/default.png')
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null = True)
    last_time_online = models.DateTimeField(auto_now_add=True)
    subscribe = models.BooleanField(default=False)
    cookie_agree = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Category(models.Model):
    category= models.CharField(max_length = 20, null=False)

    def __str__(self):
        return self.category

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=400, null=False)
    article_content = RichTextField(max_length=20000, null=False)
    article_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article_created = models.DateTimeField(auto_now_add=True)
    article_edited = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'yl/article_titles/', default='yl/article_titles/default.png')
    article_karma = models.IntegerField(default = 0 )
    article_views = models.IntegerField(default = 0 )
    article_category = models.ManyToManyField(Category)
    show_author =  models.BooleanField(default=True)

    def __str__(self):
        return self.article_title
    
    def category(self):
        categorys = []
        for item in self.article_category.all():
            categorys.append(item)
        return categorys

class Comment(models.Model):
    Comment= models.TextField(max_length = 1000 , null = False)
    article_id= models.ForeignKey(Article, on_delete=models.CASCADE)   #, null = False
    user_id= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    karma = models.IntegerField(default = 0 )