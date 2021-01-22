from django import template
from django.utils.safestring import mark_safe
import calendar

register = template.Library()

import calendar

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]

@register.filter(name='abs')
def abs_filter(value):
    return abs(value)

@register.simple_tag()
def debug_object_dump(var):
    return vars(var)

category_full = {'FOO': 'Food & Groceries', 'INC': 'Income', 'HOU': 'Housing', 'TRA': 'Transportation', 'UTL': 'Utilities', 'MED': 'Medical & Insurance', 'SAV': 'Savings', 'PER': 'Personal', 'ENT': 'Entertainment', 'EDU': 'Education', 'GIF': 'Gifts & Donations'}
category_icon = {'FOO': 'fastfood', 'INC': 'attach_money', 'HOU': 'home', 'TRA': 'directions_car', 'MED': 'health_adn_safety', 'SAV': 'savings', 'PER': 'self_improvement', 'ENT': 'tv', 'EDU': 'school', 'GIF': 'card_giftcard'}
@register.simple_tag()
def display_category_with_icon(arg):
    try:
        answer = '<span class="category__icon category__icon--' + arg + '"><span class="material-icons">' + category_icon[arg] + '</span></span>' + category_full[arg]
        return mark_safe(answer)
    except KeyError:
        return ''

@register.simple_tag()
def display_category_icon(arg):
    try:
        answer = '<span class="category__icon category__icon--' + arg + '"><span class="material-icons">' + category_icon[arg] + '</span></span>'
        return mark_safe(answer)
    except KeyError:
        return ''