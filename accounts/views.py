from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from website_settings.models import SiteSettings, MenuItem, PageSection
import datetime

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrierung erfolgreich! Bitte logge dich ein.')
            return redirect('accounts:login')  # << redirect to login, not homepage
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login erfolgreich!')
            return redirect('homepage')  # << Homepage nach Login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')  # Protected view


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil erfolgreich aktualisiert!')
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Erfolgreich ausgeloggt!')
    return redirect('homepage')


def homepage(request):
    site_settings = SiteSettings.objects.first()
    menu_items_with_sections = MenuItem.objects.filter(is_active=True).order_by('order').select_related('pagesection')

    # Da Category entfernt wurde, können wir die neuesten Blogbeiträge nicht mehr so einfach filtern.
    # Hier musst du entscheiden, wie du die "neuesten Blogbeiträge" in Zukunft definieren möchtest.
    # Eine einfache Möglichkeit wäre, alle aktiven PageSections nach Veröffentlichungsdatum zu sortieren.
    latest_blog_posts = PageSection.objects.filter(is_active=True).order_by('-publication_date')[:6]

    context = {
        'site_settings': site_settings,
        'menu_items': menu_items_with_sections,
        'latest_blog_posts': latest_blog_posts,
        'year': datetime.datetime.now().year,
    }
    return render(request, 'website_settings/homepage.html', context)