# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render 

#from django.http import HttpResponse
from django.http import Http404

from .models import Item 

def index(request):
    #return HttpResponse('<p>In Index view</p>')
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
        'items': items,
    })

def item_detail(request, id):
    #return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('THis item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
