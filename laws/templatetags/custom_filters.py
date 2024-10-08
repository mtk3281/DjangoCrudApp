from django import template

register = template.Library()

@register.filter
def newline_to_br(value):
    """Replace newlines with <br> tags."""
    return value.replace('\n', '<br>')
