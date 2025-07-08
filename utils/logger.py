import logging
import os
from datetime import datetime

def setup_logger(name: str, log_dir: str = "logs", level=logging.INFO, to_console=True) -> logging.Logger:
    """
    Creates and configures a logger with a timestamped filename.

    Parameters:
    - name (str): A name prefix for the log file and logger.
    - log_dir (str): Directory where logs will be saved.
    - level (int): Logging level (e.g., logging.INFO).
    - to_console (bool): Whether to also log to console.

    Returns:
    - logging.Logger: Configured logger instance.
    """
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(log_dir, f"{name}_{timestamp}.log")

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()  # Prevent duplicate handlers

    # File handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    # Optional console handler
    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(console_handler)

    return logger
