import logging
import os
from datetime import datetime

def setup_logger(name: str = "model_building", log_dir: str = "logs", level=logging.INFO, to_console=True) -> logging.Logger:
    """
    Creates and configures a logger that appends all logs for a given day to a daily log file.

    Parameters:
    - name (str): A name prefix for the log file and logger.
    - log_dir (str): Directory where logs will be saved.
    - level (int): Logging level (e.g., logging.INFO).
    - to_console (bool): Whether to also log to console.

    Returns:
    - logging.Logger: Configured logger instance.
    """
    os.makedirs(log_dir, exist_ok=True)

    # Use only date (no time) to consolidate logs for a day
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = os.path.join(log_dir, f"{name}_{date_str}.log")

    # Create or get logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers during reuse
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_filename, mode="a")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)

        # Optional console handler
        if to_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(console_handler)

    return logger
