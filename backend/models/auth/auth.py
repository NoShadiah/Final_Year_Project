from models.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from flasgger import swag_from
from flask import  jsonify, request, Blueprint

from models.admins.model import Admin
from models.users.model import User


auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
#admin login
@auth.route("/login", methods=["POST"])
@swag_from('../documentation/docs/admin/login.yaml')
def login():
    U_email = request.json['email']
    u_pasword = request.json['password']
    Admin_Code = request.json['code']

    if not U_email or not u_pasword:
        return jsonify({"message": "All fields are required"})

    admin = Admin.query.filter_by(email=U_email).first()
    user = User.query.filter_by(email=U_email).first()

    if not admin and not user:

        return jsonify({"message": "Email does not exist"})

    elif admin: 
        # Verify the provided password against the stored hashed password
        validate = check_password_hash(admin.password,u_pasword)
    
        if validate:
            if not Admin_Code:
                return jsonify({"message":"Please enter your code"})
            elif Admin_Code != admin.company_code:
                return jsonify({"message":"Invalid company code"})
            else:
        
                access_token = create_access_token(identity=admin.A_Id)  # to create JWT for authentication
                refresh_token = create_refresh_token(identity=admin.A_Id)  # to create JWT to refresh authentication
                return {
                    "message":f'{admin.F_name}, you have successfully logged in',
                    "access_token": f"{access_token}",
                    "refresh_token": f"{refresh_token}",
                    "user_type": admin.admin_type
                }     
        else:
            return jsonify({"message": "provided incorrect password"}) 
    elif user: 
        # Verify the provided password against the stored hashed password
        validate = check_password_hash(user.password,u_pasword)
    
        if validate:
                
                access_token = create_access_token(identity=user.U_Id)  # to create JWT for authentication
                refresh_token = create_refresh_token(identity=user.U_Id)  # to create JWT to refresh authentication
                return {
                    "message":f'{user.F_name}, you have successfully logged in',
                    "access_token": f"{access_token}",
                    "refresh_token": f"{refresh_token}",
                    "user_type": user.user_type
                }     
        else:
            return jsonify({"message": "provided incorrect password"})


    
    
     
        

        
    
