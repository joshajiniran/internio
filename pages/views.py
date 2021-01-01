from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.template.defaultfilters import slugify
from django.contrib import messages
from .models import Contact, Job, BlogPost, Company, Category
from .forms import CommentForm, ContactForm, JobForm, EmailSubscriptionForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random
from django.db.models import Q
# Create your views here.


def IndexPage(request):
    #search_keys = ['searchByTitle', 'searchByLocation']
    search_jobs = request.GET.getlist('search')
    if(search_jobs):
        jobs = Job.objects.filter(Q(title__icontains=search_jobs[0]) & Q(
            category__title__icontains=search_jobs[1]) & Q(location__icontains=search_jobs[2]))
    else:
        jobs = Job.objects.all().order_by('-date_created')

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')[:4]
    categories = Category.objects.all()
    total_jobs_count = Job.objects.all().count()

    page = request.GET.get('page', 1)

    paginator = Paginator(jobs, 10)
    try:
        jobss = paginator.page(page)
    except PageNotAnInteger:
        jobss = paginator.page(1)
    except EmptyPage:
        jobss = paginator.page(paginator.num_pages)

    context_object_name = {'blog_posts': blog_posts, 'jobss': jobss,
                           'categories': categories, 'total_jobs_count': total_jobs_count}
    return render(request, 'pages/index.html', context_object_name)


def AboutPage(request):
    context_object_name = {'title': 'About'}
    return render(request, 'pages/about.html', context_object_name)


def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Message Sent Successfully')
            return redirect('homepage')
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'title': 'Contact', 'form': form})


def BlogPage(request):
    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = {'title': 'Blog', 'blog_posts': blog_posts}
    return render(request, 'pages/blog.html', context_object_name)
# class BlogPostList(generic.ListView):
#     query_set = BlogPost.objects.filter(status=1).order_by('-created_on')
#     template_name = 'pages/blog.html'

# class SingleBlogPost(generic.DetailView):
#     model = BlogPost
#     template_name = 'pages/blog-single.html'


def SingleBlogPost(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_post
            new_comment.save()
            messages.success(request, 'Comment Added Successfully!')
            return redirect('homepage')
    else:
        recents = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]
        comments = blog_post.comments.filter(active=True)
        comment_count = blog_post.comments.count()
        comment_form = CommentForm()
    #common_tags = BlogPost.tags.all()[:4]

    return render(request, 'pages/blog-single.html', {'blog_post': blog_post, 'comments': comments, 'recents': recents, 'comment_form': comment_form})


def SingleJob(request, pk):
    job = get_object_or_404(Job, pk=pk)
    categories = Category.objects.all()
    return render(request, 'pages/job-single.html', {'job': job, 'categories': categories})


@login_required
def NewPost(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Job Created Successfully',
                             extra_tags='alert alert-success')
            return redirect('homepage')
    else:
        form = JobForm()
    return render(request, 'pages/newpost.html', {'title': 'Post a Job', 'form': form})
    # if request.method == "POST":
    #     form = JobForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         messages.success(request, 'Job Created Successfully', extra_tags='alert alert-success')
    #         return redirect('newpost')
    #         #return HttpResponseRedirect('/')
    #     else:
    #         form = JobForm()
    #     return render(request, 'pages/newpost.html', {'title':'Post a Job', 'form':form})


def EmailSubscribe(request):
    if request.method == "POST":
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Subscription Added Successfully!')
            return redirect('homepage')
    else:
        form = EmailSubscriptionForm()
    return render(request, 'pages/master.html', {'f': form})


def CompaniesList(request):
    companies = Company.objects.filter(verified=True)
    return render(request, 'pages/companies.html', {'companies': companies})

# this is where the post list magic happens....


def SingleCompanyDetail(request, pk, slug):
    company = get_object_or_404(Company, pk=pk, slug=slug)
    jobs = Job.objects.filter(company=company).order_by('-date_created')
    return render(request, 'pages/company-single.html', {'company': company, 'jobs': jobs})


def GetUserProfile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'account/userprofile.html', {'user': user})


def GetSingleCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    jobs_for_this_category = Job.objects.filter(category=category)
    return render(request, 'pages/category-single.html', {'category': category, 'jobs_for_this_category': jobs_for_this_category})
# def NewBlogPost(request):
#     if request == "POST":
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             newblogpost = form.save(commit=False)
#             newblogpost.slug = slugify(newblogpost.title)
#             newblogpost.save()
#             #Now save the tags..
#             form.save_m2m()
#             context = {
#                 'form':form,
#             }
#             return render(request, 'pages/newblogpost.html', context)
