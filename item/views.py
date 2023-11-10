from django.shortcuts import render
from .models import Category, Item
def item(request):
    pass


def detail(request,pk):
    item=Item.objects.all()
    item=Item.objects.get(id=pk)
    context={
        'item':item,
    }
    return render(request, 'item/detail.html',context)