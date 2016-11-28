from django import forms
from django.utils.translation import ugettext_lazy as _
from geekjobs.models import Job

"""
class JobForm(forms.Form):
    title = forms.CharField(label='Job title', max_length=380)
    city = forms.CharField(label='City', max_length=100, required=False)
    state = forms.ChoiceField(label='State', choices=DE_STATE_CHOICES)
    remote = forms.BooleanField(label='Remote', required=False)
    salary = forms.CharField(label='Salary', max_length=100, required=False)
    description = forms.CharField(label='Job Description', max_length=10000)
    description.widget = forms.HiddenInput()
    instructions = forms.CharField(label='How do people apply for this job?', max_length=380)
    instructions.widget = forms.Textarea(attrs={'rows': 3})
    name = forms.CharField(label='Company Name', max_length=100)
    url = forms.CharField(label='Job URL', max_length=150)
    email = forms.EmailField(label='Email')
"""


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'city', 'state', 'remote', 'salary', 'description', 'instructions', 'name', 'url', 'email')
        widgets = {
            'description': forms.HiddenInput,
            'instructions': forms.Textarea(attrs={'rows': 3})
        }
        labels = {
            'title': _('Job Title'),
            'city': _('City'),
            'state': _('State'),
            'remote': _('Remote'),
            'salary': _('Salary'),
            'description': _('Job Description'),
            'instructions': _('How do people apply for this job?'),
            'name': _('Company Name'),
            'url': _('Job URL'),
            'email': _('Email')
        }
