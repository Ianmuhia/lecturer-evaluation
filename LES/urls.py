from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from rating.views import barView, SizesView
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("questions", include("questions.urls")),
    path("accounts/", include("accounts.urls")),
    path("answerd/", include("answerd.urls")),

    path("contacts/", include("contacts.urls")),
    
    path("rating", include("rating.urls")),
    path("admin/", admin.site.urls),
    url(r"^$", barView.as_view(template_name="home.html"), name="home"),
    url(r"^sizes$", SizesView.as_view(), name="sizes"),
    url(r"^ratings/", include("star_ratings.urls", namespace="ratings")),
]
