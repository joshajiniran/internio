from django.forms import ModelForm, TextInput, Textarea, RadioSelect, Select, FileInput   
from django import forms
from .models import Contact, Job, EmailSubscription, BlogPost



class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField()
    # class Meta:
    #     model = EmailSubscription
    #     fields = ('email',)
    #     widgets = {
    #         'email': TextInput(attrs = {'class':'form-control', 'placeholder':'Enter email address'}),
    #         }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(attrs = {'class':'form-control', 'placeholder':'Your Name'}),
            'email': TextInput(attrs = {'class':'form-control', 'placeholder':'Your Email'}),
            'subject': TextInput(attrs = {'class':'form-control', 'placeholder':'Subject', 'placeholder':'Subject'}),
            'message': Textarea(attrs = {'class':'form-control', 'cols':'30', 'rows':'7', 'placeholder':'Your Message'})
        }



class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'company', 'category', 'job_type', 'location', 'description', 'job_company_image')

        widgets = {
            'title': TextInput(attrs = {'id':'fullname', 'class':'form-control', 'placeholder':'eg. Professional UI/UX Designer'}),
            'company': TextInput(attrs = {'id':'fullname', 'class':'form-control', 'placeholder':'eg. Facebook, Inc.'}),
            'category': Select(attrs ={'id':'jobcategory', 'class':'form-control'}),
            'job_type': RadioSelect(attrs = {'id':'option-job-type-1', 'class':'', 'name':'job-type'}),
            'location': TextInput(attrs = {'id':'', 'class':'form-control', 'placeholder':'Western City, UK'}),
            'description': Textarea(attrs = {'id':'', 'class':'form-control', 'cols':'30', 'rows':'5'}),
            'job_company_image': FileInput(attrs = {'id':'image', 'class':'form-control'}),
        }

        # default_data = {
        #     'category': 'Job Category', 'job_type': 'Job Type'
        #     }


# class BlogPostForm(ModelForm):
#     class Meta:
#         model = BlogPost

#         fields = [
#             'title',
#             'body',
#             'author',
#             'feature_image',
#             'comments_count',
#             'status',
#             'tags',
#         ]
        



        