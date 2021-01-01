from django.contrib import admin
<<<<<<< HEAD
from .models import Contact, Job, EmailSubscription, BlogPost, Category, Company, Comment
# Register your models here.

=======
from .models import (
    Contact, Job, EmailSubscription, BlogPost, Category,
    Company, Comment, Profile
)
# Register your models here.


>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
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
<<<<<<< HEAD
    search_fields = ('title', 'job_type', 'category__title', 'location', 'description')
=======
    search_fields = ('title', 'job_type', 'category__title',
                     'location', 'description')

>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_subscribed'
    )

    list_filter = ('email', 'date_subscribed')
    search_fields = ('email', 'date_subscribed')


<<<<<<< HEAD

=======
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'body',
        'author',
        'feature_image',
        'created_on',
<<<<<<< HEAD
        'comments_count', 
=======
        'comments_count',
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
        'status',
        # 'tags',
    )
    list_filter = ('title', 'author', 'created_on')
    search_fields = ('title', 'body', 'author', 'created_on')
<<<<<<< HEAD
    prepopulated_fields = {'slug':['title',]}

    actions = ['publish_blog_post']


=======
    prepopulated_fields = {'slug': ['title', ]}

    actions = ['publish_blog_post']

>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
    def publish_blog_post(self, request, queryset):
        queryset.update(status=1)


<<<<<<< HEAD

=======
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
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

<<<<<<< HEAD
    list_filter = ('company_name', 'company_email', 'company_location', 'company_date_created', 'verified')
    search_fields = ('company_name', 'company_email', 'company_location', 'company_date_created', 'verified')
    prepopulated_fields = {'slug':['company_name',]}   
    actions = ['verify_company']


=======
    list_filter = ('company_name', 'company_email',
                   'company_location', 'company_date_created', 'verified')
    search_fields = ('company_name', 'company_email',
                     'company_location', 'company_date_created', 'verified')
    prepopulated_fields = {'slug': ['company_name', ]}
    actions = ['verify_company']

>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
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
<<<<<<< HEAD
=======


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
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
