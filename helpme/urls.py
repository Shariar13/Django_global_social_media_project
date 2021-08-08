
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('adminpanel.urls')),
    path('signin/',include('sign.urls')),
    path('profile/',include('post.urls')),
    path('chat/', include('chat.urls')),
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
