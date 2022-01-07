import os
from flask_migrate import Migrate
from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config_manager.config_manager import FileConfigManager
from utils.request_controller import RequestsController


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p@192.168.43.141:5432/collaboration_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


if 'L2_CONFIG_PATH' in os.environ and os.environ['L2_CONFIG_PATH'] != 'None':
    configs = FileConfigManager(os.environ.get('L2_CONFIG_PATH'))
else:
    print('No Configuration Manager Found')


db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


from routes import collaboration
from models.model_collaboration import Collaboration_Model


# Collaboration API Signatures
api.add_resource(collaboration.CollaborationAPI, '/this_is_test_api_for_collaborate')

# API Signature for Comment
api.add_resource(collaboration.CommentReadUpdateDelete, '/comments')
api.add_resource(collaboration.CommentWrite, '/comments')

# API Signature for Feedback
api.add_resource(collaboration.FeedbackWrite, '/feedback')
api.add_resource(collaboration.FeedbackRead, '/feedback')
