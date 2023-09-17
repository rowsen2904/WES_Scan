import os

environment = os.getenv("DJANGO_SETTINGS", "local")

if environment == "local":
    from .local import *
else: 
    from .production import *