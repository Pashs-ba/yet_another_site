from django import template
from core.models import Category

register = template.Library()

@register.simple_tag(takes_context=True)
def category_all(context):
    context['category_list'] = Category.objects.all()
    return ''