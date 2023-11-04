from django import template
from apps.treemenu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name)
    
    if menu_items.exists():
        menu = menu_items.first()
        menu_items = menu.get_descendants(include_self=True).filter(level__lte=0)

        context['menu_items'] = menu_items

    return ''