from datetime import datetime
from dataclasses import dataclass
from models.db import db

@dataclass
class Application(db.Model):
    __tablename__ = "applications"

    id: int 
    A_Id: str
    Student_Id: str 
    Internship_Id: str
    cover_letter: str
    introductory_letter: str
    curriculum_vitae: str
    Application_status: str 
    Application_date: str

    id = db.Column(db.Integer, unique = True, nullable=False) 
    A_Id = db.Column(db.String(10), primary_key=True)
    Student_Id = db.Column(db.String(10), db.ForeignKey("student_profiles.SP_Id")) 
    Internship_Id = db.Column(db.String(5), db.ForeignKey("internships.IN_Id"))
    cover_letter = db.Column(db.String(200), nullable=False, unique=True)
    introductory_letter = db.Column(db.String(200), nullable=False, unique=True)
    curriculum_vitae = db.Column(db.String(200), nullable=False, unique=True)
    Application_status = db.Column(db.String(10), nullable=False) 
    Application_date = db.Column(db.String(20), default=datetime.now())    