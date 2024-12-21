from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
