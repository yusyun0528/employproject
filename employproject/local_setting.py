import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'sc37qt40u-6d)2j_!er@0_7ym^n0mo5i_8dkxnqmeb2*b576*s'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True