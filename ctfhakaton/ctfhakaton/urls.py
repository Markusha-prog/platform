from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profileuser.urls')),
    path('', include('homepage.urls')),
]
