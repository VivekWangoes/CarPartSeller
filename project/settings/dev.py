from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default=5433, cast=int),
    }
}


# EMAIL_BACKEND = 'django_ses.SESBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS',default=True, cast=bool)
# EMAIL_PORT = config('EMAIL_PORT',default=25, cast=int)
# EMAIL_USE_SSL = config('EMAIL_USE_SSL',default=False, cast=bool)
# EMAIL_SENDER = config('EMAIL_SENDER')

EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_SENDER = 'localhost'
EMAIL_PORT = 1025