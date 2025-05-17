# menu/templatetags/menu_tags.py
from django import template
from django.urls import reverse
from django.utils.html import format_html
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    # Один запрос к БД для получения всех пунктов меню
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')

    def build_menu(items, active_item=None):
        html = '<ul>'
        for item in items:
            is_active = False
            target_url = None

            # Определяем URL для пункта меню
            if item.url:
                target_url = item.url
            elif item.named_url:
                try:
                    target_url = reverse(item.named_url)
                except Exception:
                    target_url = "#"

            # Убедимся, что URL начинается с "/"
            if not target_url.startswith('/'):
                target_url = '/' + target_url

            # Проверяем, является ли пункт активным
            if target_url and target_url == current_path:
                is_active = True

            css_class = 'active' if is_active else ''
            html += f'<li class="{css_class}">'

            # Ссылка
            if target_url:
                html += f'<a href="{target_url}">{item.name}</a>'
            else:
                html += f'<span>{item.name}</span>'

            # Рекурсивно добавляем дочерние элементы
            if item.children.exists():
                html += build_menu(item.children.all(), active_item=item if is_active else None)

            html += '</li>'

        html += '</ul>'
        return html

    return format_html(build_menu(menu_items))