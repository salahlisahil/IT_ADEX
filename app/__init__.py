from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile('config.py')

# LOG TURN OFF
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
log.disabled = True

# MAIN DB
from app.models import db
db.init_app(app)

# MAIN FLASK MIGRATION
migrate = Migrate(app, db)

# BLUEPRINTS CONNECT
from app.routes import base_bp
app.register_blueprint(base_bp)

from app.routes import project_bp
app.register_blueprint(project_bp)

from app.routes import action_bp
app.register_blueprint(action_bp)


# UTILS CONNECT
from app.utils import admin
admin.init_app(app)

from app.utils import moment
moment.init_app(app)

from app.utils import mail
mail.init_app(app)

