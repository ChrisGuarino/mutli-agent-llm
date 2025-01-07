import logging

# Set up logging
logging.basicConfig(
    filename="file_mover.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(message, error=False):
    """
    Logs actions and errors to the log file.
    """
    if error:
        logging.error(message)
    else:
        logging.info(message)