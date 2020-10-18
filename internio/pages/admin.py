from django.contrib import admin
from .models import Contact, Job, EmailSubscription, BlogPost, Categories
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_created'
    )
    list_filter = ('email', 'date_created')
    search_fields = ('email', 'date_created')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'job_type',
        'location',
        'description',
        'date_created'
    )

    list_filter = ('company', 'location', 'date_created')
    search_fields = ('title', 'job_type', 'location', 'description')

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_subscribed'
    )

    list_filter = ('email', 'date_subscribed')
    search_fields = ('email', 'date_subscribed')



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'body',
        'author',
        'feature_image',
        'created_on',
        'comments_count',
        'status'
    )
    list_filter = ('title', 'author', 'created_on')
    search_fields = ('title', 'body', 'author', 'created_on')
    prepopulated_fields = {'slug':['title',]}

    actions = ['publish_blog_post']


    def publish_blog_post(self, request, queryset):
        queryset.update(status=1)



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
        'jobs'
    )
    list_filter = ('title', 'date_created', 'jobs')
    search_fields = ('title', 'date_created', 'jobs')