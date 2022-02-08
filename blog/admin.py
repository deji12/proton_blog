from django.contrib import admin
from .models import Post, category, Comment, NewsletterReg


# Register your models here.
admin.site.register(Post)
admin.site.register(category)
admin.site.register(Comment)
admin.site.register(NewsletterReg)
