# Generated by Django 5.2 on 2025-05-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_settings', '0013_remove_sitesettings_active_theme_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettingsColors',
            fields=[
            ],
            options={
                'verbose_name': 'Farben',
                'verbose_name_plural': 'Farben',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('website_settings.sitesettings',),
        ),
        migrations.CreateModel(
            name='SiteSettingsLogo',
            fields=[
            ],
            options={
                'verbose_name': 'Logo & Position',
                'verbose_name_plural': 'Logo & Position',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('website_settings.sitesettings',),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
