import dj_database_url

from .settings import *

DEBUG = True

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += [
  # 'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = '2pj0w-+ouhi&!^pkdt*nnc#$*zv$zmbkm)qsh(#uit!&hn%_*&'

ALLOWED_HOSTS = ['dogomodel.herokuapp.com', 'localhost']
