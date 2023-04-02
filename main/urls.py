
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from shop.views import home,Register
from django.views.generic.base import TemplateView
urlpatterns = [
    path('register/success/',TemplateView.as_view(template_name='registration/success.html'),name='register-success'),
    path('register/',Register.as_view(),name='register'),
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',home,name='home'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)