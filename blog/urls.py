from django.urls import path
from .views import BlogHome, Login, Register, AdminPage, LogoutAdmin, CreatePost, ArticleDetailView, CategoryView, Categories, replycomment, AllPost, AddCat, AD, Admin, TopPost, WeekEmail, AboutUs, DeletePost, EditPost, AllEmails


urlpatterns = [
    path('', BlogHome, name="blog-home"),
    path('dashboard-login/', Login, name="dashboard-login"),
    path('register-dashboard/', Register, name="register-dashboard"),
    path('dash/', AdminPage, name="dashboard"),
    path('logout/', LogoutAdmin, name="logout"),
    #path('<int:id>/', Article, name="article-page"),
    path('all-posts/', AllPost, name='all-post'),
    path('post_detail/<slug:slug>/', AD, name="article-page"),
    path('create-post/', CreatePost, name="create-post"),
    path('add-category/', AddCat, name="add_category"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('categories/', Categories, name='all_categories'),
    path('blog/<int:id>/reply-comment/', replycomment.as_view(), name="reply-comment"),
    path('admin-page/', Admin, name='admin-page'),
    path('top-post/', TopPost, name='top-post'),
    path('admin/blog/post/<int:pk>/change/', Admin, name='edit-post'),
    path('weekly-email-register/', WeekEmail, name='week-email'),
    path('about-us/', AboutUs, name='about-us'),
    path('admin/blog/post/', DeletePost, name='delete-post'),
    path('admin/blog/post/', EditPost, name='edit-post'),
    path('admin-page/all-emails/', AllEmails, name='all-emails')
]