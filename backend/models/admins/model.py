from models.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Admin(db.Model):
    __tablename__ = 'admins'

    # representation of columns on retrieval
    id: int
    A_Id: str
    F_name: str
    L_name: str
    age: int
    gender: str
    email: str
    contact: int
    address: str
    password: str
    company_code: str
    Reg_at: str
    updated_at: str

    id = db.Column(db.Integer, unique=True, nullable=False)
    A_Id = db.Column(db.String(2), primary_key=True)
    F_name= db.Column(db.String(20), nullable=False)
    L_name= db.Column(db.String(20), nullable=False)
    age= db.Column(db.Integer, nullable=False)
    gender= db.Column(db.String(6), nullable=False)
    email= db.Column(db.String(50), nullable=False, unique = True)
    contact= db.Column(db.String(10), nullable=False, unique = True)
    address= db.Column(db.String(100), nullable=False)
    password= db.Column(db.String(30), unique = True, nullable=False)
    company_code = db.Column(db.String(8), unique=True, nullable=False)
    admin_type= db.Column(db.String(15), unique = True, nullable = False, default = "Manager")
    profile_image= db.Column(db.String(200), nullable = False, default = "https://media.istockphoto.com/id/1313958250/vector/user-avatar-profile-icon-black-vector-illustration-on-transparent-background-website-or-app.jpg?s=170667a&w=0&k=20&c=jWdfqd_wjXbteDFLeMaaKwknZYyia6RHWKU3zosiinI=")
    Reg_at = db.Column(db.String(30), nullable=False, default=datetime.now())
    updated_at = db.Column(db.String(30), nullable=True, onupdate=datetime.now())

    # relationships
    user_roles = db.relationship("UserRole", backref="admin", lazy="dynamic")
    sub_fields = db.relationship("Sub_Field", backref="admin", lazy="dynamic")
    company_profiles = db.relationship("CompanyProfile", backref="admin", lazy="dynamic")
    internships = db.relationship("InternShip", backref="admin", lazy="dynamic")
    question_categories = db.relationship("InterviewQuestionCategory", backref="admin", lazy="dynamic")
    interview_questions = db.relationship("InterviewQuestion", backref="admin", lazy="dynamic")
    tips = db.relationship("Tip", backref="admin", lazy="dynamic")
    reviews = db.relationship("Review", backref="admin", lazy="dynamic")
    frequently_asked_questions = db.backref("FAQ", backref="admin", lazy="dynamic")
    messages = db.relationship("Message", backref="admin", lazy="dynamic")

    # def __init__(self, 
    #              A_Id, 
    #              F_name,
    #              L_name,
    #              age,
    #              gender, 
    #              email, 
    #              Contact, 
    #              Address, 
    #              password,
    #              company_code,
    #              admin_type,
    #              profile_image,
    #              Reg_at,
    #              updated_at ):
    #     self.A_Id = A_Id 
    #     self.F_name = F_name
    #     self.L_name = L_name
    #     self.age = age
    #     self.gender =  gender
    #     self.email =  email
    #     self.Contact =  Contact
    #     self.Address =  Address
    #     self.password = password
    #     self.company_code = company_code
    #     self.admin_type = admin_type
    #     self.profile_image = profile_image
    #     self.Reg_at = Reg_at
    #     self.updated_at = updated_at

    # def __repr__(self):
    #     return f"<{self.admin_type} {self.L_name} {self.F_name}>"