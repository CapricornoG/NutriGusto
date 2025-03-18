from django.contrib import admin
from django.urls import path
from home.views import index  # Import the home page view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Add the home page route
]
