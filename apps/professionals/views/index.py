from django.shortcuts import render
from django.db.models import Count
from ..models import Category
from ..selectors import professional_get_featured

def index(request):
    categories = Category.objects.annotate(pro_count=Count('professionals'))
    featured = professional_get_featured(6)

    context = {
        'categories': categories,
        'featured': featured,
    }
    return render(request, 'professionals/index.html', context)
