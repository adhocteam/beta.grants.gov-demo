from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

def currency(dollars):
    return f"${intcomma(int(dollars))}"

register.filter('currency', currency)
