# coding: utf-8

from django import forms
from . import models


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        exclude = ['ordinal', ]
        widgets = {
            'reviewer': forms.HiddenInput(),
            'post': forms.HiddenInput(),
            'rating': forms.RadioSelect(),
        }
