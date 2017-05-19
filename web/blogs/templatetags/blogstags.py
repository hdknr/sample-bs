# -*- coding: utf-8 -*-
from django import template
from blogs import forms

register = template.Library()


@register.simple_tag(takes_context=False)
def review_form(user, post):
    return forms.ReviewForm(
        None, initial={'reviewer': user, 'ware': post})
