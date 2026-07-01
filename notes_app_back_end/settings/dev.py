from .common import *

DEBUG = True

SECRET_KEY = "django-insecure-^$^g+7g9t=a)zc2rbm7o*ap5zgx@v=x2=@^a&3ilpb1fvwry$1"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "70.153.137.156",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}