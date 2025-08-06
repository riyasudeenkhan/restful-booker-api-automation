import logging

def setup_logger():
    logger = logging.getLogger("booking_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("booking.log", mode='w')
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
