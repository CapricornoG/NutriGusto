from django.contrib import admin
from django.urls import path, include  
from home.views import index  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  
    path('', index, name='home'),  
]
