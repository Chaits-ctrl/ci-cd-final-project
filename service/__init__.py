from flask import Flask

app = Flask(__name__)

# Importing after creating the Flask app
from service import routes              
from service.common import log_handlers 

# Initialize logging with gunicorn error log
log_handlers.init_logging(app, log_name="gunicorn.error")

# Logging service start message
app.logger.info("*" * 70)
app.logger.info(" S E R V I C E   R U N N I N G ".center(70, "*"))
app.logger.info("*" * 70)

if __name__ == "__main__":
    app.run()
