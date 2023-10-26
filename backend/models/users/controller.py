#register a new user
import random
from flask import  jsonify, request, Blueprint
from models.emailSender import Verify_email
from models.users.model import User
from models.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from flasgger import swag_from
# from models.app2 import key

from email.message import EmailMessage

import ssl
import smtplib

users = Blueprint('users', __name__, url_prefix='/api/v1/users')

# #user login
# @users.route("/token", methods=["POST"])
# @swag_from('../documentation/docs/user/login.yaml')
# def login():
#     email = request.json.get("email")
#     user_password = request.json.get("password")
#     user = User.query.filter_by(email=email).first()

#     if not email or not user_password:
#         return jsonify({"message": "All fields are required"})
#     if user:
        
#         def password():
#             u_password = user_password
        
#             password_hashed = user.password
#             validate=check_password_hash(password_hashed, u_password)
#             if validate:
#                 access_token = create_access_token(identity=user.id) #to make JSON Web Tokens for authentication
#                 refresh_token = create_refresh_token(identity=user.id) #to make JSON Web Tokens to refresh authentication
#                 return {"access_token":f"{access_token}",
#                         "refresh_token":f"{refresh_token}",
#                         "user_type":user.user_type}
#             else:
#                 return "Provided an incorrect password"
#         return password()
#     else:
#         return "Email does not exist"   
        

        
    

# #get all users
# @users.route("/all")
# @jwt_required()
# def all_users():
#     user_logged_in=get_jwt_identity()
#     check_user_details = User.query.filter_by(id=user_logged_in).first()
#     userType = check_user_details.user_type
#     if userType == "client" or userType == "customer":
#         return {"message":"Sorry but access denied, you are unauthorized"}
    

#     else:
#         users = User.query.all()
#         response = [{
#             "Id":user.id,
#             "First name":user.F_name, 
#             "Last name":user.L_name,
#             "Email":user.email,
#             "Contact":user.contact,
#             "User type":user.user_type ,
#             "Gender":user.gender,
#             "Address":user.address,
#             "Registered at":user.registered_at,
#             "Updated at":user.updated_at
#         }for user in users]
#         return jsonify(
#                 response),200
    


@users.route('/register',methods=['POST'])
def create_user():
    user_fname =request.json['f_name']
    user_lname = request.json['l_name']
    user_email = request.json['email']
    user_contact =request.json['contact']  
    user_password = request.json['password']
    user_user_type=request.json['user_type']
    user_gender = request.json['gender']
    user_address = request.json['address']
    U_verification_code = request.json['code']
    password_hash = generate_password_hash(user_password)
  


    # validations
    #getting the user a data
    if not user_fname:
        return jsonify({'Message':"First name is required"}),400

    if not user_lname:
        return jsonify({'Message':"Last name is required", "status code": 400}),

    if not user_contact:
        return jsonify({'Message':"Contact is required", "status code": 400})
    
    if not user_password:
        return jsonify({'Message':"Password is required","status code": 400})
    if not user_gender:
        return {"message":"Your gender is required, either male or female", "status code": 400}
    if  not user_user_type:
        default = "student"
        user_user_type = default
    
    # password validation length
    if len(user_password)<6:
        return jsonify({'Message':"Password must be atleast 6 characters long"})
    
    
    
    #constaints
    if User.query.filter_by(email=user_email).first():
       return jsonify({'Message':"Email already exists", "status code": 400})
    
    
    existing_user_contact=User.query.filter_by(contact=user_contact).first()
    if existing_user_contact:
            return jsonify({'Message':"Contact already in use", "status code": 409})
     
# email verification
    codesent = 0
    
    if not user_email:
        return jsonify({'Message':"Email is required", "status code": 400})
    
    if user_email and not U_verification_code:

        verification_code = random.randint(100095, 353637)
        codesent = verification_code

        message = f"Nice to have you here {user_fname}. Take a step further to verify y0ur email address. \n Use the this verification code {verification_code}"

        key = 'jyod ifxo obvh wopu'

        email_sender = 'nabawangashadiah20@gmail.com'
        email_key = key

        email_receiver = user_email

        subject = 'Verify your email address'
        # OTP = 

        body = message

        # creating an instance of the EmailMessage package
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        # setting a context for my mail
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_key)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            # the as_string converts the data in the EmailMessage instage as a string

            if len(U_verification_code) < 6 or U_verification_code != codesent:
                return jsonify({"message":"Invalid code", "code": codesent})


        return jsonify({"message": f"A six digit verification code has been sent to {user_email}, it is required for \n your successfull registration with Skills connect"})
    
    
        
    
    

        
    
    
    
    # model-Ids settings
    number = random.randint(1,1000000)  
    user_Id = "U"+str(number)
    finaL_user_Id = "U"+str(number)
    existing_user_id=User.query.filter_by(U_Id=user_Id).first()
    if existing_user_id:
            number = random.randint(1,3)
            user_Id = "U"+str(number)
            finaL_user_Id = user_Id
    
# Id settings, for auto increment
    N_id = 0
    max_value = User.query.with_entities(User.id).order_by(User.id.desc()).first()
    if max_value:
        max_number = max_value[0]
        increment = 1
        N_id = increment + max_number
    else:
        N_id = 1
    

    #storing new user
    new_user = User( 
                    id = N_id,
                    U_Id=user_Id,
                    F_name = user_fname,
                    L_name = user_lname,
                    email = user_email,
                    contact = user_contact,
                    password=password_hash,
                     user_type=user_user_type,
                     gender=user_gender,
                    address = user_address)
    #  address = user_address,
    

    #adding a new users to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
                    'Success':True,
                    'Message':f"{new_user.F_name} you have successfully created an account with skills connect",
                    }),201

    


# @users.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_user(user_id):
#     user = User.query.get_or_404(user_id)

#     if request.method == 'GET':
#         response = {
#             "id":user.id,
#             "name": user.F_name + user.L_name,
#             "user_type":user.user_type,
#             "email": user.email,
#             "contact": user.contact
#         }
#         return {"success": True,"message":"User details retrieved", "user": response}

#     elif request.method == 'PUT':
#         data = request.get_json()

#         if not data['first name']:
#             return jsonify({"message":"Your name is required"})

#         if not data['last name']:
#             return jsonify({"message":"Your name is required"})
        
#         if not data['email']:
#             return jsonify({"message":"Your email address is required"})
        
#         if not data['contact']:
#             return jsonify({"message":"Your contact is required"})
        
#         if not data['password'] or len(data['password'])<6:
#             return jsonify({"message":"Your password is required and must be greater than 6 characters"})
        
#         user.F_name = data['first name']
#         user.L_name = data['last name']
#         user.email = data['email']
#         user.contact = data['contact']
#         user.password = generate_password_hash(data['password'])
#         # user.updated_at = datetime.now()
#         db.session.add(user)
#         db.session.commit()
#         return {"message": f"User details of {user.F_name} updated successfully"}

#     elif request.method == 'DELETE':
#         if user is None:
#             return{"message":"User identity not found", "status code":"404"}
#         else:
#             db.session.delete(user)
#             db.session.commit()
#             return {"message": f"User {user.F_name} successfully deleted."}   
  
# # logging out a user
# # unset_jwt_cookies function which deletes the cookies containing the access token for the user
# @users.route("/logout", methods=["POST"])
# def logout():
#     response = jsonify({"message": "logout successful"})
#     unset_jwt_cookies(response)
#     return response


