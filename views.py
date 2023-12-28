from django.shortcuts import render, loader, redirect, get_object_or_404
from panel.models import Category, Dish
from django.http import HttpResponse
from .templates import *

# Create your views here.


def main_page(request):
    return render(request, 'home_page.html')

def cat_ru(request):
    cats = Category.objects.all()
    context = {
        'categories': cats,
    }
    return render(request,'categories_ru.html', context)


def cat_en(request):
    cats = Category.objects.all()
    context = {
        'categories': cats,
    }
    return render(request,'categories_en.html', context)


def dishes_ru(request, pk):
    cats = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    dishes = category.dish_set.all()
    context = {
        'categories': cats,
        'category' : category,
        'dishes' : dishes,
    }
    return render(request, 'dishes_ru.html', context)



def dishes_en(request, pk):
    cats = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    dishes = category.dish_set.all()
    context = {
        'categories': cats,
        'category' : category,
        'dishes' : dishes,
    }
    return render(request, 'dishes_en.html', context)


def cv(request):
    return render(request, 'cv.html') 
