from .base import *     # NOQA

DEBUG = False

ALLOWED_HOSTS = ['wayne-chen.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wayneblog_db',
        'USER': 'root',
        'PASSWORD': '0831',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    },
}

ADMINS = MANAGERS = (
    ('Wayne.Chen', 'waynechen1994@163.com'),
)

EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'waynechen1994@163.com'
EMAIL_HOST_PASSWORD = '39miku0831'
EMAIL_SUBJECT_PREFIX = '来自【Wayne博客】的邮件'
DEFAULT_FROM_EMAIL = 'waynechen1994@163.com'
SERVER_EMAIL = 'waynechen1994@163.com'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/logs/WayneBlog.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,    # 1M
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
