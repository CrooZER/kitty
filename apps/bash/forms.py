from django import forms
from taggit.forms import *

class ReasonForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.Textarea()
    tags = TagField()