
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('mi_blog_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('post.urls')),
    path('chats/', include('mensajeria.urls')),
    path('admin/', admin.site.urls),
]