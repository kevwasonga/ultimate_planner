from ..models import SiteStats

def site_stats(request):
    """
    Context processor that provides global site stats to all templates.
    """
    return {
        'site_stats': SiteStats.get_global_stats()
    }
