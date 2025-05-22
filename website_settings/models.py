from django.db import models
from django.utils.text import slugify
from colorfield.fields import ColorField
from tinymce.models import HTMLField


class SiteSettings(models.Model):
    menu_color = ColorField(format="hexa", default='#343a40', verbose_name='Menü-Hintergrundfarbe')
    menu_text_color = ColorField(format="hexa", default='#ffffff', verbose_name='Menü-Schriftfarbe')
    background_color = ColorField(format="hexa", default='#ffffff', verbose_name='Seitenhintergrundfarbe')
    text_color = ColorField(format="hexa", default='#000000', verbose_name='Allgemeine Textfarbe')

    logo = models.ImageField(
        upload_to='logo/',
        blank=True,
        null=True,
        verbose_name='Logo (Schriftzug)'
    )
    logo_max_height = models.IntegerField(
        default=80,
        verbose_name="Maximale Logo-Höhe (Pixel)",
        help_text="Die maximale Höhe des Logos in Pixel."
    )
    logo_vertical_shift = models.IntegerField(
        default=0,
        verbose_name="Vertikaler Logo-Versatz (Pixel)",
        help_text="Positiver Wert verschiebt das Logo nach unten, negativer nach oben."
    )
    logo_horizontal_shift = models.IntegerField(
        default=0,
        verbose_name="Horizontaler Logo-Versatz (Pixel)",
        help_text="Positiver Wert verschiebt das Logo nach rechts, negativer nach links."
    )

    def __str__(self):
        return "Website-Einstellungen"

    class Meta:
        verbose_name_plural = "Website-Einstellungen"

class SiteSettingsColors(SiteSettings):
    class Meta:
        proxy = True
        verbose_name = "Farben"
        verbose_name_plural = "Farben"

class SiteSettingsLogo(SiteSettings):
    class Meta:
        proxy = True
        verbose_name = "Logo & Position"
        verbose_name_plural = "Logo & Position"

class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Menü Titel')
    slug = models.SlugField(unique=True, blank=True, help_text='Wird für die URL und die Section-ID verwendet (automatisch generiert, kann angepasst werden)')
    order = models.IntegerField(default=0, verbose_name='Reihenfolge', help_text='Bestimmt die Reihenfolge im Menü')
    is_active = models.BooleanField(default=True, verbose_name='Aktiv')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Menüeintrag'
        verbose_name_plural = 'Menüeinträge'

class PageSection(models.Model):
    menu_item = models.OneToOneField('MenuItem', on_delete=models.CASCADE, primary_key=True, verbose_name='Menüeintrag')
    title = models.CharField(max_length=200, verbose_name='Section Überschrift', blank=True)
    # first_paragraph = HTMLField(verbose_name='Erster Absatz (Fett)', blank=True) # ENTFERNT
    content = HTMLField(verbose_name='Section Inhalt', blank=True)
    image = models.ImageField(upload_to='sections/', blank=True, null=True, verbose_name='Section Bild')
    order = models.IntegerField(default=0, verbose_name='Reihenfolge', help_text='Bestimmt die Reihenfolge der Sections auf der Seite')
    is_active = models.BooleanField(default=True, verbose_name='Aktiv')
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, blank=True, verbose_name='Autor')
    publication_date = models.DateField(null=True, blank=True, verbose_name='Veröffentlichungsdatum')

    LAYOUT_CHOICES = [
        ('one-column', 'Einspaltig'),
        ('two-columns-left', 'Zweispaltig (Bild links)'),
        ('two-columns-right', 'Zweispaltig (Bild rechts)'),
        ('paper-article', 'Paper Artikel'), # Neue Layout-Option
        # Füge hier weitere Optionen nach Bedarf hinzu
    ]

    layout = models.CharField(
        max_length=20,
        choices=LAYOUT_CHOICES,
        default='one-column',
        verbose_name='Layout'
    )

    # Textfarbe für diese Section
    section_text_color = ColorField(format="hexa", default=None, blank=True, null=True, verbose_name='Textfarbe der Section')

    # Umrandung
    BORDER_CHOICES = [
        ('', 'Keine'),
        ('border', 'Einfach'),
        ('border-top', 'Oben'),
        ('border-bottom', 'Unten'),
        ('border-left', 'Links'),
        ('border-right', 'Rechts'),
        ('border-primary', 'Primär'),
        ('border-secondary', 'Sekundär'),
        # Füge weitere Bootstrap-Border-Klassen hinzu, falls gewünscht
    ]
    border = models.CharField(max_length=20, choices=BORDER_CHOICES, blank=True, verbose_name='Umrandung')
    rounded = models.BooleanField(default=False, verbose_name='Abgerundete Ecken')
    shadow = models.BooleanField(default=False, verbose_name='Schatten')

    # Hintergrundfarbe
    background_color = ColorField(format="hexa", default=None, blank=True, null=True, verbose_name='Hintergrundfarbe')

    # Schriftstil
    FONT_WEIGHT_CHOICES = [
        ('', 'Normal'),
        ('fw-bold', 'Fett'),
        ('fw-light', 'Dünn'),
    ]
    font_weight = models.CharField(max_length=10, choices=FONT_WEIGHT_CHOICES, blank=True, verbose_name='Schriftstärke')
    font_italic = models.BooleanField(default=False, verbose_name='Kursiv')
    TEXT_ALIGN_CHOICES = [
        ('', 'Standard'),
        ('text-start', 'Links'),
        ('text-center', 'Zentriert'),
        ('text-end', 'Rechts'),
    ]
    text_align = models.CharField(max_length=11, choices=TEXT_ALIGN_CHOICES, blank=True, verbose_name='Textausrichtung')

    # Abstand (Padding und Margin - hier nur einige Beispiele, erweitere nach Bedarf)
    PADDING_CHOICES = [
        ('', 'Standard'),
        ('p-1', 'Klein (1)'),
        ('p-2', 'Mittel (2)'),
        ('p-3', 'Groß (3)'),
        ('py-2', 'Vertikal Mittel (py-2)'),
        ('px-3', 'Horizontal Groß (px-3)'),
        # Füge weitere Bootstrap-Padding-Klassen hinzu
    ]
    padding = models.CharField(max_length=10, choices=PADDING_CHOICES, blank=True, verbose_name='Padding')

    MARGIN_CHOICES = [
        ('', 'Standard'),
        ('m-1', 'Klein (1)'),
        ('m-2', 'Mittel (2)'),
        ('mb-3', 'Unten Groß (mb-3)'),
        # Füge weitere Bootstrap-Margin-Klassen hinzu
    ]
    margin = models.CharField(max_length=10, choices=MARGIN_CHOICES, blank=True, verbose_name='Margin')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Homepage Section'
        verbose_name_plural = 'Homepage Sections'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_item.title)
        super().save(*args, **kwargs)