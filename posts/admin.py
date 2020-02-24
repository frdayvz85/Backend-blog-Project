from django.contrib import admin
from .views import *

from .models import Author, Category, Post, Comment, PostView

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)



admin.site.register(About)
admin.site.register(Introduction)
admin.site.register(Footer)

# Register your models here.
