import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_message(message, level=logging.INFO):
    """
    Logs a message with the given logging level.
    :param message: The message to log.
    :param level: The logging level (default: logging.INFO).
    """
    if level == logging.DEBUG:
        logging.debug(message)
    elif level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)
    elif level == logging.CRITICAL:
        logging.critical(message)
    else:
        logging.info(message)