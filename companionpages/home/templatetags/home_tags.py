from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

import markdown

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def md(text):
    html = markdown.markdown(text, safe_mode='replace', output_format='html5')
    return mark_safe(html)
