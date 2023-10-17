from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class SavedInternship(db.Model):
    id: int
    SIM_ID: str
    Student_Id: str
    Internship_Id: str
    status: str #can be saved and applied, 
    Made_at: str

    id = db.Column(db.Integer, unique = True, nullable=False)
    SIM_ID = db.Column(db.String(10), primary_key=True)
    Student_Id = db.Column(db.String(6), db.ForeignKey("student_profiles.SP_Id"))
    Internship_Id = db.Column(db.String(5), db.ForeignKey("internships.IN_Id"))
    status = db.Column(db.String(60)) #can be saved and applied, 
    Made_at = db.Column(db.String(60), default=datetime.now())