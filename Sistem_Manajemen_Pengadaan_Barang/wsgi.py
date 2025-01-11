"""
WSGI config for Sistem_Manajemen_Pengadaan_Barang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sistem_Manajemen_Pengadaan_Barang.settings')

application = get_wsgi_application()
