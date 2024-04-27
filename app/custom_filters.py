# custom_filters.py
from django import template

register = template.Library()


@register.filter
def truncate_description(description):
    words = description.split()
    truncated_description = ' '.join(words[:15])
    if len(words) > 15:
        truncated_description += ' ... <a href="#">Read more</a>'
    return truncated_description
