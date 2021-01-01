from django.contrib import admin
from .models import (
    Contact, Job, EmailSubscription, BlogPost, Category,
    Company, Comment, Profile
)
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
        'category',
        'job_type',
        'location',
        'description',
        'job_company_image',
        'date_created'
    )

    list_filter = ('company', 'location', 'category', 'date_created')
    search_fields = ('title', 'job_type', 'category__title',
                     'location', 'description')


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
        'status',
        # 'tags',
    )
    list_filter = ('title', 'author', 'created_on')
    search_fields = ('title', 'body', 'author', 'created_on')
    prepopulated_fields = {'slug': ['title', ]}

    actions = ['publish_blog_post']

    def publish_blog_post(self, request, queryset):
        queryset.update(status=1)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created'
    )
    list_filter = ('title', 'date_created')
    search_fields = ('title', 'date_created')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'slug',
        'company_phone',
        'company_email',
        'company_location',
        'company_company_image',
        'company_date_created',
        'verified'
    )

    list_filter = ('company_name', 'company_email',
                   'company_location', 'company_date_created', 'verified')
    search_fields = ('company_name', 'company_email',
                     'company_location', 'company_date_created', 'verified')
    prepopulated_fields = {'slug': ['company_name', ]}
    actions = ['verify_company']

    def verify_company(self, request, queryset):
        queryset.update(verified=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'author',
        'email',
        'body',
        'created_on',
        'active'
    )
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'linkedin',
        'github',
        'cv',
        'avatar',
        'created_on',
        'user'
    )
