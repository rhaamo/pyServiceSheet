"""pyservicesheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from baton.autodiscover import admin
from django.urls import path, include
from django.conf import settings
from controllers.utils import static
from controllers.items import views as views_items
from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
]

urlpatterns += [
    path("", views_items.home, name="category"),
    url(r"^category/(?P<category_id>[0-9a-zA-Z]+)$", views_items.home, name="category"),
    url(r"^item/(?P<item_id>[0-9a-zA-Z]+)$", views_items.item, name="item"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
