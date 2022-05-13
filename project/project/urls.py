
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    #path('news/', include('simpleapp.urls')),

    path('news/', include('protect.urls')),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]