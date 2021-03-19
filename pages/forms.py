from django.forms import ModelForm, TextInput, Textarea, RadioSelect, Select, FileInput
from django import forms

from allauth.account.forms import SignupForm

from .models import (
    Comment, BlogPost,
    Contact, Job, EmailSubscription,
    Profile
)


class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField()
    # class Meta:
    #     model = EmailSubscription
    #     fields = ('email',)
    #     widgets = {
    #         'email': TextInput(attrs = {'class':'form-control', 'placeholder':'Enter email address'}),
    #         }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'cols': '30', 'rows': '7', 'placeholder': 'Your Message'})
        }



class JobForm(ModelForm):
  
    class Meta:
        model = Job
        fields = ('title', 'company', 'category', 'job_type',
                  'location', 'description', 'job_company_image')

        widgets = {
            'title': TextInput(attrs={'id': 'fullname', 'class': 'form-control', 'placeholder': 'eg. Professional UI/UX Designer'}),
            'company': TextInput(attrs={'id': 'fullname', 'class': 'form-control', 'placeholder': 'eg. Facebook, Inc.'}),
            'category': Select(attrs={'id': 'jobcategory', 'class': 'form-control'}),
            'job_type': RadioSelect(attrs={'id': 'option-job-type-1', 'class': '', 'name': 'job-type'}),
            'location': TextInput(attrs={'id': '', 'class': 'form-control', 'placeholder': 'Western City, UK'}),
            'description': Textarea(attrs={'id': '', 'class': 'form-control', 'cols': '30', 'rows': '5'}),
            'job_company_image': FileInput(attrs={'id': 'image', 'class': 'form-control'}),
        }

        # default_data = {
        #     'category': 'Job Category', 'job_type': 'Job Type'
        #     }


# class BlogPostForm(forms.ModelForm):
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


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['organization'] = forms.CharField(required=True)
        self.fields['github'] = forms.URLField(required=True)
        self.fields['linkedin'] = forms.URLField(required=True)

    def save(self, request):
        organization = self.cleaned_data.pop('organization')
        github = self.cleaned_data.pop('github')
        linkedin = self.cleaned_data.pop('linkedin')
        ...
        user = super(MyCustomSignupForm, self).save(request, commit=True)
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')

        widgets = {
            'author': TextInput(attrs={'id': 'name', 'class': 'form-control'}),
            'email': TextInput(attrs={'id': 'email', 'class': 'form-control'}),
            'body': Textarea(attrs={'id': 'message', 'class': 'form-control', 'cols': '30', 'rows': '10'}),
        }
