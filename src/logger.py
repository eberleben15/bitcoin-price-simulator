import logging

def get_logger():
    """Configure and return a logger."""
    logger = logging.getLogger('BitcoinTrader')
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of log messages
    
    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # Add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(ch)
    
    return logger