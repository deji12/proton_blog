from django import forms
from django.forms import ModelForm
from .models import Post, category, category2

CATEGORIES = (
    ('html', 'Html'),
    ('css', 'Css'),
    ('javascript', 'Javascript'),
    ('python', 'Python')
)

choices = category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


choices2 = category2.objects.all().values_list('name', 'name')

choice_list2 = []

for item2 in choices2:
    choice_list2.append(item2)

class CreatePostForm(ModelForm):
    # category = forms.ChoiceField(choices=CATEGORIES,widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'category2', 'body', 'image', 'author_image')

        labels = {
            'title': '',
            'body': '',
            'category': '',
            'category2': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'category2': forms.Select(choices=choice_list2, attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }

class CatForm(ModelForm):
    class Meta:
        model = category
        fields = '__all__'

        labels = {
            'Category Name'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }
# class CommentForm(ModelForm):
   
#     class Meta:
#         model = Comment
#         fields = ('name', 'body',)

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
#         }