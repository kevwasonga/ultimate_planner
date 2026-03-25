from django.shortcuts import render
from django.db.models import Count
from ..models import Category

def about(request):
    categories = Category.objects.annotate(pro_count=Count('professionals'))
    return render(request, 'professionals/about.html', {
        'categories': categories,
    })
