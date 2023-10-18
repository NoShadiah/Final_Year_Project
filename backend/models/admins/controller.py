#register a new admin
import random
from flask import  jsonify, request, Blueprint
from models.admins.model import Admin
from models.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from flasgger import swag_from

admins = Blueprint('admins', __name__, url_prefix='/api/v1/admins')

#admin login
@admins.route("/token", methods=["POST"])
@swag_from('../documentation/docs/admin/login.yaml')
def login():
    email = request.json.get("email")
    admin_password = request.json.get("password")
    admin = Admin.query.filter_by(email=email).first()

    if not email or not admin_password:
        return jsonify({"message": "All fields are required"})
    if admin:
        
        def password():
            u_password = admin_password
        
            password_hashed = admin.password
            validate=check_password_hash(password_hashed, u_password)
            if validate:
                access_token = create_access_token(identity=admin.id) #to make JSON Web Tokens for authentication
                refresh_token = create_refresh_token(identity=admin.id) #to make JSON Web Tokens to refresh authentication
                return {"access_token":f"{access_token}",
                        "refresh_token":f"{refresh_token}",
                        "admin_type":admin.admin_type}
            else:
                return "Provided an incorrect password"
        return password()
    else:
        return "Email does not exist"   
        

        
    

#get all admins
# @admins.route("/all")
# @jwt_required()
# def alL_admins():
#     admin_logged_in=get_jwt_identity()
#     check_admin_details = Admin.query.filter_by(A_Id=admin_logged_in).first()
#     adminType = check_admin_details.admin_type
#     if adminType == "assistant":
#         return {"message":"Sorry, you are unauthorized"}   

#     else:
#         admins = Admin.query.all()
#         response = [{
#             "Id":admin.id,
#             "Admin_Id":admin.A_Id,
#             "First name":admin.F_name, 
#             "Last name":admin.last_name,
#             "Email":admin.email,
#             "Contact":admin.contact,
#             "admin type":admin.admin_type ,
#             "Gender":admin.gender,
#             "Address":admin.address,
#             "Company code": admin.company_code,
#             "Registered at":admin.registered_at,
#             "Updated at":admin.updated_at
#         }for admin in admins]
#         return jsonify(response),200

@admins.route('/register',methods=['POST'])
def create_Admin():
    
    admin_fname =request.json['firstname']
    admin_lname = request.json['lastname']
    admin_age = request.json['age']
    admin_gender = request.json['gender']
    admin_email = request.json['email']
    admin_contact =request.json['contact']
    admin_address = request.json['address']  
    admin_password = request.json['password']
    admin_type=request.json['admin_type']
    admin_company_code = request.json['company_code']
    admin_profile_pic = request.json['profile_pic']
    password_hash = generate_password_hash(admin_password)
  


    # validations
    #getting the admin a data
    if not admin_fname:
        return jsonify({'Message':"First name is required, 400"})

    if not admin_lname:
        return jsonify({'Message':"Last name is required, 400"})
    
    if not admin_age:
        return jsonify({'Message':"Age is required, 400"})
    
    if not admin_gender:
        return {"message":"Gender is required, either male or female"}
    
    if not admin_address:
        return jsonify({'Message':"Address is required, 400"})
    
    
    
    
    # email validation
    if not admin_email:
        return jsonify({'Message':"Email is required", "exit code": "400"})
    elif Admin.query.filter_by(email=admin_email).first():
       return jsonify({'Message':"Email already in use"}),409
    
    # Contact validation
    if not admin_contact:
        return jsonify({'Message':"Contact is required, 400"})
    elif Admin.query.filter_by(contact=admin_contact).first():
            return jsonify({'Message':"Contact already in use", "Exit code":"409"})
       
    # password vlidation   
    if not admin_password:
        return jsonify({'Message':"Password is required, 400"})
    elif len(admin_password)<6:
        return jsonify({'Message':"Password must be atleast 6 characters long"})
    elif admin_email==admin_password or admin_contact == admin_password:
        return jsonify({"Message":"For security of your account, the following should not be used as passwords\n 1. Email \n 2. Contact \n 3. Your names \n These credentials can be easily guessed by unauthorized personnels"})

    # Admin type validation
    if not admin_type:
        return jsonify({"Message":"Admin type is required, 400"})
    elif Admin.query.filter_by(admin_type=admin_type).first():
        return jsonify({"Message":"Can't have two admins with the same privileges 100%"})    
    
    #company code validation
    if not admin_company_code:
        return jsonify({'Message':"Company code is required"})
    elif len(admin_company_code)<8:
        return jsonify({'Message':"Company code 8 characters long"})
    elif Admin.query.filter_by(company_code=admin_company_code).first():
       return jsonify({'Message':"Company code already exists"}),409
    
    
    
# model-Ids settings
    number = random.randint(1,3)  
    admin_Id = "A"+str(number)
    finaL_admin_Id = "A"+str(number)
    existing_admin_id=Admin.query.filter_by(A_Id=admin_Id).first()
    if existing_admin_id:
            number = random.randint(1,3)
            admin_Id = "A"+str(number)
            finaL_admin_Id = admin_Id
    
# Id settings, for auto increment
    N_id = 0
    max_value = Admin.query.with_entities(Admin.id).order_by(Admin.id.desc()).first()
    if max_value:
        max_number = max_value[0]
        increment = 1
        N_id = increment + max_number
    else:
        N_id = 1
    
    #storing new admin
    new_admin = Admin( id=N_id,
                    A_Id=finaL_admin_Id,
                    F_name = admin_fname,
                    L_name = admin_lname,
                    age = admin_age,
                    gender=admin_gender,
                    email = admin_email,
                    contact = admin_contact,
                    address = admin_address,
                    password = password_hash,
                    admin_type = admin_type,
                    company_code = admin_company_code,
                    profile_image=admin_profile_pic
                    )
    #  address = admin_address,
    

    #adding a new admins to the database
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({
                    'Success':True,
                    'Message':f"{new_admin.F_name} you have successfully created a new Admin account",
                    "Exit code": "201"})


# @admins.route('/admin/<admin_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_Admin(admin_id):
#     admin = Admin.query.get_or_404(admin_id)

#     if request.method == 'GET':
#         response = {
#             "id":admin.id,
#             "name": admin.F_name + admin.last_name,
#             "admin_type":admin.admin_type,
#             "email": admin.email,
#             "contact": admin.contact
#         }
#         return {"success": True,"message":"admin details retrieved", "admin": response}

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
        
#         admin.F_name = data['first name']
#         admin.last_name = data['last name']
#         admin.email = data['email']
#         admin.contact = data['contact']
#         admin.password = generate_password_hash(data['password'])
#         # admin.updated_at = datetime.now()
#         db.session.add(admin)
#         db.session.commit()
#         return {"message": f"admin details of {admin.F_name} updated successfully"}

#     elif request.method == 'DELETE':
#         if admin is None:
#             return{"message":"admin identity not found", "status code":"404"}
#         else:
#             db.session.delete(admin)
#             db.session.commit()
#             return {"message": f"admin {admin.F_name} successfully deleted."}   
  
# # logging out a admin
# # unset_jwt_cookies function which deletes the cookies containing the access token for the admin
# @admins.route("/logout", methods=["POST"])
# def logout():
#     response = jsonify({"message": "logout successful"})
#     unset_jwt_cookies(response)
#     return response


