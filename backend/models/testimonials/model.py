from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Testimonial(db.Model):
    __tablename__ = "testimonials"

    id: int
    T_ID: str
    U_Id: str
    Testimaonial_text: str
    Internship_Id: str
    reg_at: str

    id = db.Column(db.Integer, nullable = False, unique = True)
    T_ID = db.Column(db.String(6), primary_key=True)
    U_Id = db.Column(db.String(5), db.ForeignKey("users.U_Id"))
    Testimaonial_text = db.Column(db.Text, unique=True, nullable=False)
    Internship_Id = db.Column(db.String(5), db.ForeignKey("internships.IN_Id"))
    reg_at = db.Column(db.String(30), default=datetime.now())