LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(module)s: %(message)s ',
        },
        'json': {
            '()': 'json_log_formatter.JSONFormatter'
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/general.log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 3,
            'formatter': 'default',
        },
        'request': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/observer.log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 5,
            'formatter': 'json',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'propagate': False,
            'level': 'INFO',
        },
        'observer': {
            'handlers': ['request'],
            'propagate': False,
            'level': 'INFO',
        }
    }
}