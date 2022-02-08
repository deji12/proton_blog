from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000000)
    slug = models.SlugField(default='test')
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(default='Body')
    id = models.IntegerField(primary_key=True)
    #tags = TaggableManager()
    image = models.ImageField(blank=True, null=True, upload_to='image/')
    author_image = models.ImageField(blank=True, null=True, upload_to='author/', default='images/tpg.jpg')
    category = models.CharField(max_length=128, default='Python')
    # category = models.CharField(max_length=255, default='Python')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    num_clicks = models.IntegerField(default=0)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article-page', args=[self.id])

class Comment(models.Model):  
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name


    def get_absolute_url(self):
        return reverse('blog-home')

# class ReplyComment(models.Model):
#     com = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     reply = models.TextField()
    

class NewsletterReg(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name