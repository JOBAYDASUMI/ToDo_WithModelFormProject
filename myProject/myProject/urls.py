
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('dashboardPage/',dashboardPage,name='dashboardPage'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
