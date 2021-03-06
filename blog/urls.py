from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('blog', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft_list, name='post_draft_list'),
    path('blog/post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/post/<pk>/remove/', views.post_remove, name='post_remove'), 

]