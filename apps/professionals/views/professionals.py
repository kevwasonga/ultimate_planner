from django.shortcuts import render
from ..models import Category
from ..selectors import professional_list

def professionals_list(request, category_slug=None):
    """
    View to display a filtered list of professionals.
    """
    search = request.GET.get('search', '')
    location = request.GET.get('location', '')

    queryset = professional_list(search=search, category_slug=category_slug, location=location)
    
    categories = Category.objects.all()
    selected_category = Category.objects.filter(slug=category_slug).first() if category_slug else None

    context = {
        'professionals': queryset,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search,
        'location_query': location,
    }
    return render(request, 'professionals/list.html', context)
