
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mi_blog_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('post.urls')),
    path('chats/', include('mensajeria.urls')),
    path('admin/', admin.site.urls),
]