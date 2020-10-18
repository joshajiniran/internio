from django.db import models
from django.contrib.auth.models import User
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



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ['Contacts']

    def __str__(self):
        return '{} {} {}'.format(self.name, self.email, self.subject)


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='+')
    job_type = models.CharField(max_length=100, choices=CATEGORIES, default="Permanent")
    location = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Jobs'

    def __str__(self):        
        return '{} {} {} '.format(self.title, self.company, self.location)

class Categories(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{}'.format(self.title)


class EmailSubscription(models.Model):
    email = models.CharField(max_length=100)
    date_subscribed = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ['Email Subscription Lists']

    def __str__(self):      
        return '{}'.format(self.email)        

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    feature_image = models.FileField(upload_to='gallery/', null=True)
    created_on = models.DateField(auto_now_add=True)
    comments_count = models.IntegerField()
    status = models.IntegerField(choices=POST_STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']     

    def __str__(self):
        return '{}'.format(self.title)





