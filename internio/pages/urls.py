from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='homepage'),
    path('about', views.AboutPage, name='about'),
    path('contact', views.ContactPage, name='contact'),
    path('blog', views.BlogPage, name='blog'),
    path('blog/<slug:slug>/', views.SingleBlogPost, name='singlepost'),
    path('newpost', views.NewPost, name='newpost'),
]