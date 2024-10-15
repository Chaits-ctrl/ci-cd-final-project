"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Import log handlers first
from service.common import log_handlers

# Initialize logging after importing handlers
log_handlers.init_logging(app, "gunicorn.error")

# Import routes after log handlers are initialized
from service import routes

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
