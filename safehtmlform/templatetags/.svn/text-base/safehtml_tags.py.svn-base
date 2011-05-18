from django import template
from safehtmlform.utils import sanitize_html

register = template.Library()

def safehtml(value, arg=None):
    return sanitize_html(value)
register.filter('safehtml', safehtml)
