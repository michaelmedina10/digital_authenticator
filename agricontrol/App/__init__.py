from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# storage for tag img just work in static folder 
app = Flask(__name__,static_url_path='/static')
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type = True) 

manager = Manager(app)
manager.add_command('db', MigrateCommand)
db.create_all()
app.config ['SEND_FILE_MAX_AGE_DEFAULT'] = 0
from App.Controllers import routes