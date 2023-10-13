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
    upd_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)

    def __init__(self,
                CP_Id,
                company_contact,
                company_name,
                industry,
                location,
                website,
                linkedIn,
                whatsapp,
                github,
                bitbucket, 
                email,
                profile_pic,
                reg_at,
                reg_by,
                upd_at):
                
                self.CP_Id= CP_Id
                self.company_contact= company_contact
                self.company_name = company_name
                self.industry= industry
                self.location= location
                self.website= website
                self.linkedIn= linkedIn
                self.whatsapp= whatsapp
                self.github= github
                self.bitbucket=  bitbucket
                self.email= email
                self.profile_pic= profile_pic
                self.reg_at = reg_at
                self.reg_by = reg_by
                self.upd_at = upd_at


    def __repr__(self):
            return f"<Company profile: {self.company_name} is a {self.industry}"
