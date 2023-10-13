from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CompanyProfile(db.Model):
    __tablename__ = "company_profiles"

    id:int
    CP_Id: str
    Company_Contact: str
    Industry: str
    Location: str
    website: str
    LinkedIn: str
    Whatsapp: str
    Github: str
    Bitbucket: str 
    email: str
    profile_pic: str
    Reg_at: str
    Reg_by: str
    upd_at: str


    id = db.Column(db.String(), nullable=False, unique=True)
    CP_Id = db.Column(db.String(), nullable=False, unique=True) 
    Company_Contact = db.Column(db.String(), nullable=False, unique=True) 
    Industry = db.Column(db.String(), nullable=False, unique=True) 
    Location = db.Column(db.String(), nullable=False) 
    website = db.Column(db.String(), nullable=False, unique=True) 
    LinkedIn = db.Column(db.String(), nullable=False, unique=True) 
    Whatsapp = db.Column(db.String(), nullable=False, unique=True) 
    Github = db.Column(db.String(), nullable=False, unique=True) 
    Bitbucket = db.Column(db.String(), nullable=False, unique=True) 
    email = db.Column(db.String(), nullable=False, unique=True) 
    profile_pic = db.Column(db.String(), nullable=False, unique=True) 
    Reg_at = db.Column(db.String(), nullable=False, default=datetime.now()) 
    Reg_by = db.Column(db.String(), db.ForeignKey("users.U_Id"), nullable=False)
    upd_at = db.Column(db.String(), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(), db.ForeignKey("users.U_Id"), nullable=False)

    def __init__

