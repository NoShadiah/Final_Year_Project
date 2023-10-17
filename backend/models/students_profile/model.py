from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class StudentProfile(db.Model):
    __tablename__="student_profiles"

    id: int 
    SP_Id:str
    U_Id: int
    S_Name: str
    Institution:str
    Course: str
    Sub_FOS: str
    Preferences: str  # must be one of the fields in the FOS table,
    Skills: str
    LevelOfEducation: str #e.g diploma, certificate, bachelor's deegree, masters' deegree,
    period: int
    Join_EndDate: str
    status: str
    LinkedIn: str
    Whatsapp: str
    Github: str
    Bitbucket: str
    email: str
    profile_pic: str
    reg_at: str
    reg_by: str 
    upd_at: str
    upd_by:str

    id = db.Column(db.Integer, unique=True)
    SP_Id = db.Column(db.String(10), primary_key=True) 
    U_Id = db.Column(db.String(5), db.ForeignKey("users.U_Id"), nullable = False)
    S_Name = db.Column(db.String(60), nullable = False)
    Institution = db.Column(db.String(60), nullable = False)
    Course = db.Column(db.String(30), nullable = False)
    Sub_FOS = db.Column(db.String(6),db.ForeignKey("sub_fields.SF_Id") , nullable = False)
    Preferences = db.Column(db.Text, nullable = False)  # must be one of the fields in the FOS table,
    Skills = db.Column(db.Text, nullable = False)
    LevelOfEducation = db.Column(db.String(30), nullable = False) #e.g diploma, certificate, bachelor's deegree, masters' deegree,
    period = db.Column(db.Integer, nullable=False)
    Join_EndDate = db.Column(db.String(40), nullable = False)
    status = db.Column(db.String(10), nullable = False)
    LinkedIn = db.Column(db.String(80), nullable = False, unique=True)
    Whatsapp = db.Column(db.String(10), nullable = False, unique=True)
    Github = db.Column(db.String(50), nullable = False, unique=True)
    Bitbucket = db.Column(db.String(50), nullable = False, unique=True)
    email = db.Column(db.String(50), nullable = False, unique=True) #Should be automatically generated from the users table
    profile_pic = db.Column(db.String(1200), nullable = False)
    reg_at = db.Column(db.String(20), default = datetime.now())
    reg_by = db.Column(db.String(5), db.ForeignKey("users.U_Id"))
    upd_at = db.Column(db.String(20), onupdate = datetime.now())
    upd_by = db.Column(db.String(5), db.ForeignKey("users.U_Id"))

    saved_internships = db.relationship("SavedInternships", backref="studentprofile")
    applications = db.relationship("Application", backref="studentprofile")