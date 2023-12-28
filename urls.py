from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page, name='main'),
    path('cat_ru', views.cat_ru, name='cat_ru'),
    path('cat_en', views.cat_en, name='cat_en'),
    path('dishes_ru/<int:pk>', views.dishes_ru, name='dishes_ru'),
    path('dishes_en/<int:pk>', views.dishes_en, name='dishes_en'),
    path('cv', views.cv, name='cv'),
]