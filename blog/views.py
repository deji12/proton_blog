from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.base import View
from .models import Post, Comment, category, NewsletterReg
from .forms import CreatePostForm, CatForm
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from collections import Counter
# Create your views here.

def BlogHome(request):
    feautured_post= Post.objects.all().order_by('-created')[:3]
    categories = Post.objects.all()
    post = Post.objects.all().order_by('-created')[:10]
    cats = []
    for i in categories:        
        cats.append(i.category)    
        cats.append(i.category2)    
    
    for j in cats:
        counted = cats.count(j)
        if counted > 1:
            cats.remove(j)  
    

    context = {
        'posts': post,
        'categories': cats,
        'feat': feautured_post
    }
    return render(request, 'blog/index.html', context)

def AllPost(request):
    feautured_post= Post.objects.all().order_by('-created')[:3]
    categories = Post.objects.all()
    post = Post.objects.all().order_by('-created')
    cats = []
    for i in categories:        
        cats.append(i.category)     
    
    for j in cats:
        counted = cats.count(j)
        if counted > 1:
            cats.remove(j)  
    context = {
        'posts': post,
        'categories': cats,
        'feat': feautured_post
    }
    return render(request, 'blog/all_posts.html', context)

def Login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=user_name, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user_name}')
            return redirect('dashboard')
        else:
            return HttpResponse('There was an error logging in')
    return render(request, 'blog/login.html', {})

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            return HttpResponse('Wrong password!')
        else:
            pass

        if '-superuser' in username:
            splitted = username.split("-")
            sname = splitted[0]
            user = User.objects.create_superuser(sname, email, pass2)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, f'Account successfully created for {fname}. Login now')
            return redirect('dashboard-login')
        else:
            return redirect('blog-home')

    return render(request, 'blog/register.html', {})

def LogoutAdmin(request):
    logout(request)
    return redirect('dashboard-login')

@login_required
def AdminPage(request):
    return render(request, 'blog/admin.html', {})


def AD(request, slug):
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_body = request.POST.get('body')

        new_comment = Comment(name=name, body=comment_body)
        new_comment.post = Post.objects.get(slug=slug)
        new_comment.save()
        return redirect('article-page', slug=slug)    
    


    data = Post.objects.get(slug=slug)
    comments = data.comments.all().order_by('-date')

    #save number of clicks
    data.num_clicks += 1
    data.save()
    
    data2 = Post.objects.all().order_by('-created')[:10]
    feautured_post= Post.objects.all().order_by('-created')[:3]
    categories = Post.objects.all()
    cats = []
    for i in categories:        
        cats.append(i.category)     
    
    for j in cats:
        counted = cats.count(j)
        if counted > 1:
            cats.remove(j)  

    context = {
        'data': data,
        'posts': data2,
        'feat': feautured_post,
        'categories': cats,
        'comments': comments
    }
    return render(request, 'blog/article_detail2.html', context)

class replycomment(DetailView):
    
    template_name = 'blog/comment_reply.html'

    def get_object(self):
        id_  = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)

@login_required
def CreatePost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post was successfully published!!!')

        else:
            form = CreatePostForm
            

    form = CreatePostForm
    return render(request, 'blog/post create.html', {'form': form})


# class AddCategoryView(CreateView, LoginRequiredMixin):
#     login_url = 'dashboard-login/'
#     redirect_field_name = 'dashboard-login/'
#     model = category
#     template_name = 'blog/add_category.html'
#     fields = '__all__'

@login_required
def AddCat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    form = CatForm
    context = {
        'form': form,
        }
    return render(request, 'blog/add_category.html', context)

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'blog/categories.html', {'cats': category_posts})

def Categories(request):
    feautured_post= Post.objects.all().order_by('-created')[:3]
    post = Post.objects.all().order_by('-created')[:10]
    categories = Post.objects.all()
    cats = []
    for i in categories:        
        cats.append(i.category)   
        cats.append(i.category2)  
    
    for j in cats:
        counted = cats.count(j)
        if counted > 1:
            cats.remove(j)            
       
    #print(cats)
    context = {
        'posts': post,
        'categories': cats,
        'feat': feautured_post
        }
   
    return render(request, 'blog/all_categories.html', context)








class ArticleDetailView(DetailView):
    # model = Comment
    # form_class = CommentForm
    #fields = '__all__'

    template_name = 'blog/article_detail.html'
    queryset = Post.objects.all()

    def get_object(self):
        id_  = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)

    def post(self, request, id):
        if request.method == 'POST':
            name = request.POST.get('name')
            comment_body = request.POST.get('body')

            new_comment = Comment(name=name, body=comment_body)
            
            new_comment.post = Post.objects.get(id=id)
            new_comment.save()
            return redirect('article-page', id=id)

@login_required
def Admin(request):

    post = Post.objects.all()
    post2 = Post.objects.all().order_by('-created')
    comments = Comment.objects.all()
    users = User.objects.all()

    #number of posts
    number_of_posts = 0
    for i in post:
        number_of_posts+=1    

    #number of comments
    number_of_comments = 0
    for i in comments:
        number_of_comments+=1

    #number of clicks
    nums = []
    number_of_clicks = 0
    for i in Post.objects.all().values('num_clicks'):
        nums.append(i.get('num_clicks'))
    
    final = 0
    for j in nums:
        final+=j

    #number of users
    number_of_users = 0
    for i in users:
        number_of_users+=1

    if request.method == 'POST':
        search = request.POST['search']

        try:
            check = Post.objects.get(title=search)
            name = search
            clicks = check.num_clicks
            dp = check.created

           
            comments = check.comments.all()
            fi = 0
            for i in comments:
                fi+=1         
                
            

            context = {
                'title': name,
                'clicks': clicks,
                'dp': dp,
                'num_post': number_of_posts,
                'num_comments': number_of_comments,
                'num_clicks': final,
                'num_users': number_of_users,
                'com': fi,
                'check': check
            }
            return render(request, 'blog/search.html', context)
        except:
            messages.error(request, 'Post does not exist!')
            return render(request, 'blog/search.html')
    

    #date published
    all_date = []
    post = Post.objects.all().order_by('-created')
    for i in post:
        all_date.append(i.created)

    #slug 
    # all_slug = []
    # post = Post.objects.all().order_by('-created')
    # for j in post:
    #     all_slug.append(j.slug)

    # for t in all_slug:
    #     print(t)

    #individual clicks
    nums = []
    for i in Post.objects.all().order_by('-created'):
        nums.append(i.num_clicks)
    
    #top posts
    all_slugs = []
    post = Post.objects.all().order_by('-num_clicks')
    for j in post:
        all_slugs.append(j.slug)

    #individual top clicks
    nums2 = []
    for i in Post.objects.all().order_by('-num_clicks'):
        nums2.append(i.num_clicks)

    #post and clicks 
    nums3 = []
    for j in Post.objects.all().order_by('-num_clicks'):
        nums3.append(j.num_clicks)

    all_slugss = []
    post = Post.objects.all().order_by('-num_clicks')
    for k in post:
        all_slugss.append(k.slug)

    #num comments
    fin = []
    for i in Post.objects.all().order_by('-created'):
        data = Post.objects.get(id=i.id)
        comments = data.comments.all()
        fi = 0
        for i in comments:
            fi+=1         
        
        fin.append(fi)

    context = {
        'num_post': number_of_posts,
        'num_comments': number_of_comments,
        'num_clicks': final,
        'num_users': number_of_users,
        'date_pub': all_date,
        'slug': post2,
        'clicks': nums,
        # 'top_post': comp,
        'top_clicks': nums2,
        'post': post,
        'coms': fin,
    }
    return render(request, 'blog/admin.html', context)

@login_required
def TopPost(request):
    post = Post.objects.all()
    post2 = Post.objects.all().order_by('-num_clicks')
    comments = Comment.objects.all()
    users = User.objects.all()

    # user = get_user_model().objects.values()
    # print(user)

    #number of posts
    number_of_posts = 0
    for i in post:
        number_of_posts+=1    

    #number of comments
    number_of_comments = 0
    for i in comments:
        number_of_comments+=1

    #number of clicks
    nums = []
    number_of_clicks = 0
    for i in Post.objects.all().values('num_clicks'):
        nums.append(i.get('num_clicks'))
    
    final = 0
    for j in nums:
        final+=j
        

    #number of users
    number_of_users = 0
    for i in users:
        number_of_users+=1

    #date published
    all_date = []
    post = Post.objects.all().order_by('-num_clicks')
    for i in post:
        all_date.append(i.created)

    #slug 
    all_slug = []
    post = Post.objects.all().order_by('-num_clicks')
    for j in post:
        all_slug.append(j.slug)

    #individual clicks
    nums = []
    for i in Post.objects.all().order_by('-num_clicks'):
        nums.append(i.num_clicks)
    
    #top posts
    all_slugs = []
    post = Post.objects.all().order_by('-num_clicks')
    for j in post:
        all_slugs.append(j.slug)

    #individual top clicks
    nums2 = []
    for i in Post.objects.all().order_by('-num_clicks'):
        nums2.append(i.num_clicks)   

    #num comments
    fin = []
    for i in Post.objects.all().order_by('-num_clicks'):
        data = Post.objects.get(id=i.id)
        comments = data.comments.all()
        fi = 0
        for i in comments:
            fi+=1         
        
        fin.append(fi)
    
    context = {
        'num_post': number_of_posts,
        'num_comments': number_of_comments,
        'num_clicks': final,
        'num_users': number_of_users,
        'date_pub': all_date,
        'slug': post2,
        'clicks': nums,
        'top_post': all_slugs,
        'top_clicks': nums2,
        'coms': fin,
    }
    return render(request, 'blog/top_post.html', context)

def WeekEmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        try:
            check = NewsletterReg.objects.get(email=email)
            if check:
                messages.error(request, f'{email} exists in database. Use another Email!')
                return render(request, 'blog/week_email.html')
        except:
            new_sub = NewsletterReg(name=name, email=email)
            new_sub.save()
            return redirect('blog-home')
    return render(request, 'blog/week_email.html')

def AboutUs(request):    
    data2 = Post.objects.all().order_by('-created')[:10]
    feautured_post= Post.objects.all().order_by('-created')[:3]
    categories = Post.objects.all()
    cats = []
    for i in categories:        
        cats.append(i.category)     
    
    for j in cats:
        counted = cats.count(j)
        if counted > 1:
            cats.remove(j)  

    context = {
        'posts': data2,
        'feat': feautured_post,
        'categories': cats,
    }

    return render(request, 'blog/about.html', context) 

def DeletePost(request):
    pass

def EditPost(reuest):
    pass