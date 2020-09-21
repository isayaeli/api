"""setups URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bit_api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('beats', BeatView)
router.register('instrument', InstrumentView)
router.register('Guitar', GuitarView)
router.register('Piano', PianoView)
router.register('Marimba', MarimbaView)
router.register('Trumpets', TrumpetsView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 

if settings.DEBUG:
    urlpatterns += static(
         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

