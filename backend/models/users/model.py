from models.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User(db.Model):
  __tablename__ = 'users'

  id: int
  U_Id: str
  F_name: str
  L_name: str
  age: int
  gender: str
  email: str
  contact: int
  address:str
  user_type: str


  id = db.Column(db.Integer, unique=True, nullable=False)
  U_Id = db.Column(db.String(5), primary_key = True, unique=True)
  F_name = db.Column(db.String(100),nullable=False)
  L_name = db.Column(db.String(100),nullable=False)
  gender = db.Column(db.String(6), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)  
  contact = db.Column(db.String(200), nullable=False, unique=True)
  address = db.Column(db.String(200), nullable=False)
  user_type = db.Column(db.String(100),default="student")
  password = db.Column(db.String(20), unique=True, nullable=False)
  registered_at = db.Column(db.String(200),nullable=True, default=datetime.now(), unique=True)
  updated_at = db.Column(db.String(200),nullable=True, onupdate=datetime.now(), unique=True)
  
  company_profiles = db.relationship("CompanyProfile",backref="user")
  


  def __init__(self, U_Id, F_name, L_name, email,contact,user_type,password, gender, address, age):
   self.U_Id = U_Id
   self.F_name = F_name
   self.L_name = L_name
   self.age = age
   self.email = email
   self.contact = contact
   self.user_type = user_type
   self.password = password
   self.gender = gender
   self.address = address
   

  def __repr__(self):
        return f"<User {self.L_name} {self.F_name}>"
  

        
   
 
 