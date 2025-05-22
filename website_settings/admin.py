from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import SiteSettings, MenuItem, PageSection
from colorfield.fields import ColorField, ColorWidget
from tinymce.widgets import TinyMCE


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = (
        ("Farben", {
            'fields': (
                'menu_color',
                'menu_text_color',
                'background_color',
                'text_color',
            ),
            'classes': ('collapse',),
        }),
        ("Logo-Einstellungen", {
            'fields': (
                'logo',
                'logo_max_height',
                'logo_vertical_shift',
                'logo_horizontal_shift',
            ),
            'classes': ('collapse',),
        }),
    )

    def menu_color_display(self, obj):
        return self.color_preview(obj.menu_color)
    menu_color_display.short_description = "Menü-Hintergrund"

    def background_color_display(self, obj):
        return self.color_preview(obj.background_color)
    background_color_display.short_description = "Seiten-Hintergrund"

    def text_color_display(self, obj):
        return self.color_preview(obj.text_color)
    text_color_display.short_description = "Textfarbe"

    def menu_text_color_display(self, obj):
        return self.color_preview(obj.menu_text_color)
    menu_text_color_display.short_description = "Menü-Schriftfarbe"

    def color_preview(self, color_code):
        return format_html(
            '<div style="width: 100px; height: 20px; background-color: {}; border: 1px solid #ccc;"></div><span style="margin-left: 10px;">{}</span>',
            color_code,
            color_code,
        )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'pagesection_link')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    def pagesection_link(self, obj):
        if hasattr(obj, 'pagesection') and obj.pagesection:
            url = reverse('admin:website_settings_pagesection_change', args=[obj.pagesection.pk])
            return format_html('<a href="{}">{}</a>', url, obj.pagesection.title)
        return '-'
    pagesection_link.short_description = 'Section'


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_item', 'is_active', 'layout', 'background_color', 'section_text_color', 'border', 'shadow', 'rounded')
    list_editable = ('is_active',)
    autocomplete_fields = ['menu_item']
    # 'first_paragraph' wurde aus search_fields entfernt
    search_fields = ('title', 'content', 'author')
    date_hierarchy = 'publication_date'

    # 'get_fields' ist nicht mehr notwendig, da 'first_paragraph' entfernt wurde
    # def get_fields(self, request, obj=None):
    #     fields = super().get_fields(request, obj)
    #     if obj and obj.layout == 'paper-article':
    #         new_fields = list(fields)
    #         new_fields.remove('content')
    #         new_fields.insert(new_fields.index('image'), 'content')
    #         return new_fields
    #     return fields

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = TinyMCE()
        # 'first_paragraph' wird nicht mehr in diesem Teil behandelt
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('menu_item', 'title', 'is_active', 'order', 'layout'),
        }),
        ('Inhalt', {
            # 'first_paragraph' wurde entfernt
            'fields': ('content', 'image'),
        }),
        ('Darstellung', {
            'fields': (
                'background_color',
                'section_text_color',
                'border',
                'rounded',
                'shadow',
                'font_weight',
                'font_italic',
                'text_align',
                'padding',
                'margin',
            ),
            'classes': ('collapse',),
        }),
        ('Meta-Informationen', {
            'fields': ('author', 'publication_date'),
        }),
    )