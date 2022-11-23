"""
Django settings for myweb project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# 1. os, environ, pymysql import 진행
import os
import pymysql
import environ

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. 각 호출자가 기본 매개변수를 전달할 필요가 없도록 환경 변수의 체계 기반 조회를 제공합니다
# 즉, 환경변수를 불러올 수 있는 상태로 변화한 것(connection 객체라고 생각해주시면 됩니다.)
env = environ.Env(DEBUG=(bool, True))

# 3. 환경변수가 들어있는 파일을 읽어옵니다.
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

pymysql.install_as_MySQLdb()

# 4. 환경변수를 불러옵니다.
SECRET_KEY = env('SECRET_KEY')
ALGORITHM = env('ALGORITHM')
DEBUG = env('DEBUG')

DATABASES = {
    'default' : {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : env('DB_NAME'),
        'USER'    : env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST'    : env('DB_HOST'),
        'PORT'    : env('DB_PORT'),
        'OPTIONS' : {'charset': 'utf8mb4'}
    }
}

#새로운 User 모델을 정의함에 따라 settings.py에 AUTH_USER_MODEL=’app이름.User’ 설정 값을 추가해야함
AUTH_USER_MODEL='user.User'


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []


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
    'knox',
    'user',
] 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 순서 중요
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

# CORS Settings
# 모든 접근을 허락함 - 제한하고 싶다면 'CORS_ALLOWED_ORIGINS=['168.127.0.1']'과 같이 작성
CORS_ORIGIN_ALLOW_ALL = True
# 쿠키 정보를 같이 받을건지에 대한 Boolean
CORS_ALLOW_CREDENTIALS = True

# CORS를 통해 요청받을 수 있는 http 메소드
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

# 요청을 받을 때 헤더에 담길 수 있는 정보 명시
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# DRF setting - 예시입니다.
REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "knox.auth.TokenAuthentication",
    ),

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}


ROOT_URLCONF = 'myweb.urls'

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

WSGI_APPLICATION = 'myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
