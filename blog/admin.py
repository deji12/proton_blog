from django.contrib import admin
from .models import Post, category, Comment, NewsletterReg, category2


# Register your models here.
admin.site.register(Post)
admin.site.register(category)
admin.site.register(category2)
admin.site.register(Comment)
admin.site.register(NewsletterReg)
