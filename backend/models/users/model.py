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
  # age: int
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
  # age = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)  
  contact = db.Column(db.String(200), nullable=False, unique=True)
  address = db.Column(db.String(200), nullable=False)
  user_type = db.Column(db.String(10),default="student")
  password = db.Column(db.Text, unique=True, nullable=False)
  registered_at = db.Column(db.String(200),nullable=True, default=datetime.now())
  updated_at = db.Column(db.String(200),nullable=True, onupdate=datetime.now())
  
  company_profiles = db.relationship("CompanyProfile",backref="user", lazy="dynamic")
  student_profiles = db.relationship("StudentProfile",backref="user", lazy="dynamic")
  reviews = db.relationship("Review",backref="user", lazy="dynamic")
  testimonials = db.relationship("Testimonial", backref = "user", lazy="dynamic")
  frequently_asked_questions = db.relationship("FAQ", backref="user", lazy="dynamic")
  messages = db.relationship("Message", backref="user", lazy="dynamic")
  


