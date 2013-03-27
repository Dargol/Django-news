from django import forms
from news.models import *

class NewsForm(forms.ModelForm):

    class Meta:
        model=News
