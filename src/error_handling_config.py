import logging


class CustomFormatter(logging.Formatter):
    grey = "\x1b[90m"
    blue = "\x1b[34m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    reset = "\x1b[0m"

    format = "%(levelname)s :: %(message)s (%(filename)s:%(lineno)d)"
    format_debug = "%(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_debug + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

stdoutHandler = logging.StreamHandler()
stdoutHandler.setLevel(logging.DEBUG)
stdoutHandler.setFormatter(CustomFormatter())

logger.addHandler(stdoutHandler)


def _error(msg):
    return logger.error(msg)


def _info(msg):
    return logger.info(msg)


def _warning(msg):
    return logger.warning(msg)


def _debug(msg):
    return logger.debug(f"DEBUG: {msg}")
