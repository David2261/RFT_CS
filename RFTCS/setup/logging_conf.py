LOGGING_CONF = {
    "disable_existing_loggers": False,
    "version": 1,
    "formatters": {
        "standart": {
            "format": "%(asctime)s - %(filename)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "exception": {
            "format": "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s((%lineno)d) - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "standart",
			"filename": '__logs__/main.log',
        },
        "dev_file": {
            "level": "NOTSET",
            "class": "logging.FileHandler",
            "formatter": "exception",
			"filename": '__logs__/error.log',
        },
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["file"],
        },
        "dev": {
            "level": "ERROR",
            "handlers": ["dev_file"],
        },
    },
}
