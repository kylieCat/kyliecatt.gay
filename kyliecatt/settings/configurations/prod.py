import os

from ..common import Common


class Prod(Common):
    SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "d7pa9s9e4tv5hi",
            'USER': 'atfacakheszars',
            'PASSWORD': os.environ.get("DB_PASSWORD"),
            'HOST': 'ec2-34-192-173-173.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
