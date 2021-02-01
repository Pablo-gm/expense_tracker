from django import template
from django.utils.safestring import mark_safe
import calendar
import datetime

register = template.Library()

import calendar

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]

@register.filter(name='abs')
def abs_filter(value):
    return abs(value)

@register.filter
def get_expense_category(self, category):
    return self.filter(expense_type__exact=category)

@register.simple_tag()
def display_percentage(value, max, decimals=1):
    try:
        percentage = (value / max) * 100
        return round(percentage, decimals)
    except:
        return ''

@register.simple_tag()
def debug_object_dump(var):
    return vars(var)

category_full = {'FOO': 'Food & Groceries', 'INC': 'Income', 'HOU': 'Housing', 'TRA': 'Transportation', 'UTL': 'Utilities', 'MED': 'Medical & Insurance', 'SAV': 'Savings', 'PER': 'Personal', 'ENT': 'Entertainment', 'EDU': 'Education', 'GIF': 'Gifts & Donations', 'UTL': 'Utilities'}
category_icon = {'FOO': 'fastfood', 'INC': 'attach_money', 'HOU': 'home', 'TRA': 'directions_car', 'MED': 'health_and_safety', 'SAV': 'savings', 'PER': 'self_improvement', 'ENT': 'tv', 'EDU': 'school', 'GIF': 'card_giftcard', 'UTL': 'build'}

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

@register.simple_tag()
def display_category_date_icon(arg):
    try:
        answer = '<div class="category__icon category__icon--DATE"><span class="category__header">' + arg.strftime("%d") + '</span><span class="category__text">' + arg.strftime("%b") + '</span></div>'
        return mark_safe(answer)
    except:
        return ''

@register.simple_tag()
def display_category_name(arg):
    try:
        return category_full[arg]
    except KeyError:
        return ''

@register.simple_tag()
def get_date_attributes(year, month, val=0):
    try:
        now = datetime.datetime.now()
        min_max_days = calendar.monthrange(year, month)
        current_day = 1

        val = int(val)
        if val > 0:
            current_day = val
        elif now.year == year and now.month == month:
            current_day = now.day    
        elif now.year >= year and now.month > month:
            current_day = min_max_days[1]

        return  mark_safe('min="{year}-{month:02d}-{min_day:02d}" max="{year}-{month:02d}-{max_day:02d}" value="{year}-{month:02d}-{current_day:02d}" '.format(year=year, month=month, min_day=min_max_days[0] + 1, max_day=min_max_days[1], current_day=current_day))
    except:
        return ''
