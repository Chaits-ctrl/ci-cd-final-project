"""
Log Handlers

This module contains utility functions to set up logging
consistently.
"""
import logging


def init_logging(app, logger_name: str):
    """Set up logging for production"""

    # Ensure logs from app.logger don't propagate to the root logger
    app.logger.propagate = False

    # Get the gunicorn logger
    gunicorn_logger = logging.getLogger(logger_name)

    # Set app logger's handlers and level to match gunicorn's logger
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # Ensure log formats are consistent across all handlers
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s",
        "%Y-%m-%d %H:%M:%S %z"
    )

    for handler in app.logger.handlers:
        handler.setFormatter(formatter)

    # Log that the logging handler has been successfully established
    app.logger.info("Logging handler established")
