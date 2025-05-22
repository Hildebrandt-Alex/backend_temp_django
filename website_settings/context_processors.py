from .models import SiteSettings, MenuItem
from .models import PageSection
from django.db.models import Prefetch


def site_settings(request):
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None

    menu_items = MenuItem.objects.filter(is_active=True).order_by('order')

    # Entfernen von active_theme_class und stattdessen nur menu_color verwenden
    menu_color = ''
    if site_settings:
        menu_color = site_settings.menu_color

    return {
        'site_settings': site_settings,
        'menu_items': menu_items,
        'menu_color': menu_color,  # Menüfarbe wird übergeben
    }

def sidebar(request):
    sidebar_widgets = SidebarWidget.objects.filter(is_active=True).order_by('order')
    latest_posts = PageSection.objects.filter(is_active=True).order_by('-publication_date')[:5] # Beispiel: Neueste 5 Beiträge
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return {
        'sidebar_widgets': sidebar_widgets,
        'latest_posts': latest_posts,
        'categories': categories,
        'tags': tags,
    }