from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CompanyProfile(db.Model):
    __tablename__ = "company_profiles"

    id:int
    CP_Id: str
    company_contact: str
    company_name:str
    industry: str
    location: str
    website: str
    linkedIn: str
    whatsapp: str
    github: str
    bitbucket: str 
    email: str
    profile_pic: str
    reg_at: str
    reg_by: str
    upd_at: str


    id = db.Column(db.Integer, nullable=False, unique=True)
    CP_Id = db.Column(db.String(5), nullable=False, unique=True, primary_key=True) 
    company_contact = db.Column(db.String(5), db.ForeignKey("users.U_Id"), nullable=False, unique=True)
    company_name = db.Column(db.String(50), nullable=False, unique=True) 
    industry = db.Column(db.String(50), nullable=False, unique=True) 
    location = db.Column(db.String(80), nullable=False) 
    website = db.Column(db.String(200), nullable=False, unique=True) 
    linkedIn = db.Column(db.String(200), nullable=False, unique=True) 
    whatsapp = db.Column(db.String(15), nullable=False, unique=True) 
    github = db.Column(db.String(200), nullable=False, unique=True) 
    bitbucket = db.Column(db.String(200), nullable=False, unique=True) 
    email = db.Column(db.String(100), nullable=False, unique=True) 
    profile_pic = db.Column(db.String(200), nullable=False, unique=True) 
    reg_at = db.Column(db.String(100), nullable=False, default=datetime.now()) 
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)
    upd_at = db.Column(db.String(100), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(2), default = "Not yet")

    