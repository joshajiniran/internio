from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='homepage'),
    path('about', views.AboutPage, name='about'),
    path('contact', views.ContactPage, name='contact'),
    path('blog', views.BlogPage, name='blog'),
    path('blog/<slug:slug>/', views.SingleBlogPost, name='singlepost'),
    path('newpost', views.NewPost, name='newpost'),
    path('jobs/<int:pk>/', views.SingleJob, name='job-detail'),
    path('companies', views.CompaniesList, name='companies'),
    path('companies/<int:pk>/<slug:slug>/', views.SingleCompanyDetail, name='company-detail'),
    path('accounts/profile/<int:user_id>', views.GetUserProfile, name='myprofile'),
]