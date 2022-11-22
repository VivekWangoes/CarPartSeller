from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', default=5433),
    }
}


# EMAIL_BACKEND = 'django_ses.SESBackend'
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS',default=True)
# EMAIL_PORT = os.environ.get('EMAIL_PORT',default=587)
# EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL',default=False)
# EMAIL_SENDER = os.environ.get('EMAIL_SENDER')



EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_SENDER = 'localhost'
EMAIL_PORT = 1025