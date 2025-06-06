# Generated by Django 5.2 on 2025-05-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_settings', '0014_sitesettingscolors_sitesettingslogo_pagesection_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesection',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='Veröffentlichungsdatum'),
        ),
    ]
