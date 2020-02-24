
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!2_#5!8hx@_xdxs5*w#!xnbdn**axlgk%8y0o-a&gm7f8fdk(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #my apps
    
      
    'posts',
    'marketing',
    #'account',

    #3 th part apps

    'ckeditor',
    'crispy_forms',
    
   # 'tinymce',
    
    'sweetify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True




LOGIN_REDIRECT_URL = 'dashboard'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



#SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'




## Tinymce
#
#TINYMCE_DEFAULT_CONFIG = {
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 20,
#    'selector': 'textarea',
#    'theme': 'modern',
#    'plugins': '''
#            textcolor save link image media preview codesample contextmenu
#            table code lists fullscreen  insertdatetime  nonbreaking
#            contextmenu directionality searchreplace wordcount visualblocks
#            visualchars code fullscreen autolink lists  charmap print  hr
#            anchor pagebreak
#            ''',
#    'toolbar1': '''
#            fullscreen preview bold italic underline | fontselect,
#            fontsizeselect  | forecolor backcolor | alignleft alignright |
#            aligncenter alignjustify | indent outdent | bullist numlist table |
#            | link image media | codesample |
#            ''',
#    'toolbar2': '''
#            visualblocks visualchars |
#            charmap hr pagebreak nonbreaking anchor |  code |
#            ''',
#    'contextmenu': 'formats | link image',
#    'menubar': True,
#    'statusbar': True,
#}

CKEDITOR_CONFIGS = {
    'default': {
        #'toolbar': 'full',
        #'height': 300,
        'width': '100%',
    },
}

CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'js/jquery.min.js')



SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'





EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



#
#
#AUTHENTICATION_BACKENDS = [
#
#    'django.contrib.auth.backends.ModelBackend',
#
#    'account.authentication.EmailAuthBackend',
#
#    'social_core.backends.facebook.FacebookOAuth2',
#
#    'social_core.backends.twitter.TwitterOAuth',
#
#    'social_core.backends.google.GoogleOAuth2',
#
#]
#
#
#
# social auth settings

#SOCIAL_AUTH_FACEBOOK_KEY = '' # Facebook App ID
#
#SOCIAL_AUTH_FACEBOOK_SECRET = '' # Facebook App Secret
#
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
#
#
#
#SOCIAL_AUTH_TWITTER_KEY = '' # Twitter Consumer Key
#
#SOCIAL_AUTH_TWITTER_SECRET = '' # Twitter Consumer Secret
#
#
#
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # Google Consumer Key
#
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # Google Consumer Secret
