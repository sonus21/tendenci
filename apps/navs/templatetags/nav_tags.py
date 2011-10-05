from datetime import datetime

from django.template import Library, TemplateSyntaxError, Variable

from base.template_tags import ListNode, parse_tag_kwargs
from navs.models import Nav

register = Library()

@register.inclusion_tag("navs/options.html", takes_context=True)
def nav_options(context, user, nav):
    context.update({
        "opt_object": nav,
        "user": user
    })
    return context

@register.inclusion_tag("navs/nav.html", takes_context=True)
def nav_nav(context, user, nav=None):
    context.update({
        "nav_object": nav,
        "user": user
    })
    return context

@register.inclusion_tag("navs/search-form.html", takes_context=True)
def nav_search(context):
    return context
    
@register.inclusion_tag("navs/navigation.html", takes_context=True)
def navigation(context, nav_id):
    nav = Nav.objects.get(id=nav_id)
    context.update({
        "nav": nav,
        "items": nav.items(),
    })
    return context

@register.inclusion_tag("navs/navigation_item.html", takes_context=True)
def nav_item(context, item):
    context.update({
        "item": item,
    })
    return context
