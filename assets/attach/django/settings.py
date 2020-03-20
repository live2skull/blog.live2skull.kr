import os
import logging

# private package
from vesk_toolkit.environment import is_running_on_aws, getenv, load_env, Environment

logger = logging.getLogger()

"""
updated:
    2020. 03. 20 : initial version

tested:
    django==2.2.1.1
    djangorestframework==3.11.0
    django-filter==2.2.0


#1. 스테이징 구분하여 설정파일 가져오기
#2. 디버깅 모드 설정, sentry 모드 설정
"""


# aws lambda (serverless) 환경 대응
if not is_running_on_aws():
    load_env()


DEBUG = getenv('DEBUG', bool, default=False) # type: bool

ALLOWED_HOSTS = []

# 디버깅 환경에서 속도 저하 방지
if not DEBUG:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    # sentry error handling
    sentry_sdk.init(
        dsn=getenv('SENTRY_SDK_DSN', str),
        integrations=[DjangoIntegration()],
        send_default_pii=True
    )

    # allowed host merge!
    ALLOWED_HOSTS += getenv('ALLOWED_HOST', str).split(';')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

## TODO: 사용자 SECRET_KEY 설정 *** 보안을 위해 반드시 랜덤 키값을 설정 ***
SECRET_KEY = ''

## TODO: 프로젝트 이름에 맞게 ROOT_URLCONF 설정
ROOT_URLCONF = '.urls'

## TODO: 프로젝트 이름에 맞게 WSGI_APPLICATION 설정
WSGI_APPLICATION = '.wsgi.application'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## TODO: 패키지 의존성에 따라 uncomment
    # 'djangorestframework' is rest_framework
    'rest_framework',
    'rest_framework.authtoken',

    # 'django-filter' is django_filters
    'django_filters',

    ## TODO: 사용자 application 추가
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT', int),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            # apply mysql.W002 warning hint
        }
    },

    # TODO: add optional (required when using api... applications)
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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


LANGUAGE_CODE = 'ko-kr'


TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
