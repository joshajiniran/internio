from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
#from taggit.managers import TaggableManager
=======
# from taggit.managers import TaggableManager
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
# Create your models here.
CATEGORIES = (
    ('fulltime', 'Full Time'),
    ('parttime', 'Part Time'),
    ('freelance', 'Freelance'),
    ('internship', 'Internship'),
    ('Temporary', 'Temporary')
)

POST_STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


<<<<<<< HEAD

=======
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return '{} {} {}'.format(self.name, self.email, self.subject)


class Job(models.Model):
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='job')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    job_type = models.CharField(max_length=100, choices=CATEGORIES, default="Permanent")
    location = models.CharField(max_length=100)
    job_company_image = models.FileField(upload_to='gallery/job-cover-images', null=True)
    description = models.TextField()
=======
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='job')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    job_type = models.CharField(
        max_length=100, choices=CATEGORIES, default="Permanent")
    location = models.CharField(max_length=100)
    description = models.TextField()
    job_company_image = models.FileField(
        upload_to='gallery/job-cover-images', null=True)
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Jobs'

<<<<<<< HEAD
    def __str__(self):        
        return '{} {} {} '.format(self.title, self.company, self.location)

=======
    def __str__(self):
        return '{} {} {} '.format(self.title, self.company, self.location)


>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
class Category(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Categories'
<<<<<<< HEAD
    def __str__(self):
        return '{}'.format(self.title)

=======

    def __str__(self):
        return '{}'.format(self.title)


>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    company_phone = models.CharField(max_length=13)
    company_email = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    company_company_image = models.FileField(upload_to='gallery/companies')
    company_date_created = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}'.format(self.company_name)

<<<<<<< HEAD
=======

>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
class EmailSubscription(models.Model):
    email = models.CharField(max_length=100)
    date_subscribed = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Email Subscription Lists'

<<<<<<< HEAD
    def __str__(self):      
        return '{}'.format(self.email)        
=======
    def __str__(self):
        return '{}'.format(self.email)

>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    body = models.TextField()
<<<<<<< HEAD
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
=======
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
    feature_image = models.FileField(upload_to='gallery/', null=True)
    created_on = models.DateField(auto_now_add=True)
    comments_count = models.IntegerField()
    status = models.IntegerField(choices=POST_STATUS, default=0)
<<<<<<< HEAD
    #tags = TaggableManager()
    
    class Meta:
        ordering = ['-created_on']     
=======
    # tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c

    def __str__(self):
        return '{}'.format(self.title)


<<<<<<< HEAD

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
=======
class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='comments')
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
    author = models.CharField(max_length=155, null=True, default='Anonymous')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)


<<<<<<< HEAD


=======
class Profile(models.Model):
    linkedin = models.CharField(max_length=128, null=True, blank=True)
    github = models.CharField(max_length=128, null=True, blank=True)
    cv = models.FileField(upload_to='documents/',
                          help_text='Advisable to use your name as filename',
                          null=True)
    avatar = models.FileField(upload_to='gallery/profiles', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile")

    def __str__(self):
        return f'Profile - {self.user.username}'
>>>>>>> bce7ba72f5868915c4a8202b46298b29d78ffe0c
