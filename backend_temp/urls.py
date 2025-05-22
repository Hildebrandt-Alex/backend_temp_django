# backend_temp/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  # Importiere die views aus deiner 'accounts'-App
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')), # Binde die URLs der 'accounts'-App unter '/accounts/' ein
    path('', accounts_views.homepage, name='homepage'), # Verwende die 'homepage'-View aus 'accounts.views'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)