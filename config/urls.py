from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customize the admin site
admin.site.site_header = "BuildConnect Admin"
admin.site.site_title = "BuildConnect"
admin.site.index_title = "Site Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('professionals.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
