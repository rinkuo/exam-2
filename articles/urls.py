from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_article, name='add-article'),
    path('category/<str:category>/', views.articles_by_category, name='articles-by-category'),
    path('<int:pk>/', views.article_detail, name='detail'),
]
