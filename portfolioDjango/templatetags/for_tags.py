from django import template

register = template.Library()


@register.simple_tag
def do_for(range_val):
    return range(range_val)
