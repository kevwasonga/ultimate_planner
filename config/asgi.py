import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
# Use .prod in production or set it via env variable

application = get_asgi_application()
