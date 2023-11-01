import os
from pathlib import Path
from dotenv import load_dotenv

import mimetypes
mimetypes.add_type("text/css", ".css", True)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-r+$45&sm1im6(9a@dgmt7en0*v5w4p$j_$3+ohx!bay6pj%2d5'

DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net']
CORS_ALLOW_ALL_ORIGINS: True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'customerapi'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'django-sql-project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django-sql-project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.getenv("DB_NAME"),
        'HOST': os.getenv("DB_SERVER"),
        'PORT': '1433',
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'OPTIONS': {
	            'driver': 'ODBC Driver 18 for SQL Server',
	        },
    }

    #To connect Azure SQL DB using MSI (Managed Service Identity)
    # {
    #     'ENGINE': 'mssql',
    #     'HOST': 'xyz.database.windows.net',
    #     'NAME': 'mydb', 
    #     'PORT': '', 
    #     'Trusted_Connection': 'no', 
    #     'OPTIONS': { 
    #         'driver': 'ODBC Driver 18 for SQL Server', 
    #         'extra_params': "Authentication=ActiveDirectoryMsi;Encrypt=yes;TrustServerCertificate=no" }
    # }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
