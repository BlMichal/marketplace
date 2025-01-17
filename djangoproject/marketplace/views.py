from django.shortcuts import render

from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'marketplace/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'marketplace/contact.html')