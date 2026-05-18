import os
import dj_database_url
from .base import *

DEBUG = False

# Render sets the RENDER_EXTERNAL_HOSTNAME environment variable
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME]
else:
    ALLOWED_HOSTS = ['*'] # Fallback for other environments or first-time setup

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
