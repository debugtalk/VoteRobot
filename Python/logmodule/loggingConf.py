#encoding=utf-8

LOGGING_MyConfig = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s [line:%(lineno)d]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'concise': {
            'format': '%(filename)s [%(lineno)d] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level':'DEBUG',
            'formatter': 'concise',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}