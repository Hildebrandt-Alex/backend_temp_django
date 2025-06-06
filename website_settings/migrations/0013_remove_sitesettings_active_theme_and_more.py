# Generated by Django 5.2 on 2025-05-09 20:05

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_settings', '0012_sitesettings_menu_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='active_theme',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='background_color',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Seitenhintergrundfarbe'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='menu_text_color',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Menü-Schriftfarbe'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='text_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=25, samples=None, verbose_name='Allgemeine Textfarbe'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='menu_color',
            field=colorfield.fields.ColorField(default='#343a40', image_field=None, max_length=25, samples=None, verbose_name='Menü-Hintergrundfarbe'),
        ),
    ]
