from django.contrib import admin
from django.urls import path
from myblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]