from django.db.models import Q, Count, Sum
from .models.professional import Professional

def professional_list(*, search=None, category_slug=None, location=None):
    """
    Selector to get a list of professionals based on filters.
    """
    queryset = Professional.objects.select_related('category').prefetch_related('reviews')
    
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search) |
            Q(specialty__icontains=search) |
            Q(bio__icontains=search)
        )
    
    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)
        
    if location:
        queryset = queryset.filter(location__icontains=location)
        
    return queryset

def professional_get_featured(count=6):
    """
    Selector for homepage featured professionals with fallback.
    """
    featured = Professional.objects.filter(is_featured=True, is_verified=True)[:count]
    if featured.count() < count:
        featured_ids = featured.values_list('id', flat=True)
        additional = Professional.objects.filter(is_verified=True).exclude(id__in=featured_ids)[:count - featured.count()]
        return list(featured) + list(additional)
    return featured

def professional_get_detail(pk):
    """
    Selector for a single professional.
    """
    return Professional.objects.select_related('category').prefetch_related('reviews').get(pk=pk)
