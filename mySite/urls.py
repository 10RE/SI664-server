"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_ROOT = os.path.join(BASE_DIR, 'index')
INDEX_PAGE_ROOT = os.path.join(INDEX_ROOT, 'index.html')

SITES_ROOT = os.path.join(BASE_DIR, 'sites')

SWORDFISH_ROOT = os.path.join(BASE_DIR, 'swordfish-bebop')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    url(r'^sites/(?P<path>.*)$', serve,
        {'document_root': SITES_ROOT, 'show_indexes': True},
        name='sites_path'
    ),
    url(r'^swordfish-bebop/(?P<path>.*)$', serve, 
        {'document_root': SWORDFISH_ROOT, 'show_indexes': True},
        name='swordfish-bebop'
    ),
    path('polls/', include('polls.urls')),
    path('guess/', include('guess.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('gadgets/', include('gadgets.urls')),
    url(r'^index/(?P<path>.*)$', serve,
        {'document_root': INDEX_PAGE_ROOT, 'show_indexes': True},
        name='index_path'
    ),
]
"""

import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),  # Change to ads.urls
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep

    path('ads/', include('ads.urls')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
