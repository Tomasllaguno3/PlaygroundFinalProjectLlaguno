from django.urls import path
from mi_blog_app.views import home

urlpatterns = [
    path('', home, name='home'),
]