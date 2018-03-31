"""
WSGI config for dog_odel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dog_odel.settings")

# application = Cling(get_wsgi_application())

application = get_wsgi_application()
