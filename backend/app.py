# Import flask and datetime module for showing date and time
from flask import Flask
from models import create_app, db
from models.admins.model import Admin
from models.user_roles.model import UserRole
from models.FieldCategories.model import Sub_Fields
from models.users.model import User
# import datetime
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
  
# x = datetime.datetime.now()
  
app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db, 
               Admin = Admin,
               UserRole = UserRole,
               Sub_Fields=Sub_Fields,
               User = User
               )