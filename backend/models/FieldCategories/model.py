from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Sub_Fields(db.Model):
    __tablename__ = "sub_fields"

    id: int
    SF_Id:str
    Title: str
    description: str
    FOS: str
    sample_image: str
    reg_at:str
    reg_by: str
    upd_at: str
    upd_by: str


    id = db.Column(db.Integer, nullable=False, unique=True)
    SF_Id = db.Column(db.String(6), nullable=False, primary_key=True)
    Title = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=True)
    FOS = db.Column(db.String(30), nullable=False)
    sample_image = db.Column(db.String(100), nullable=False, unique=True)
    reg_at = db.Column(db.String(30), default=datetime.now())
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"),nullable=False)
    upd_at = db.Column(db.String(30), onupdate=datetime.now())
    upd_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)

    student_profiles=db.relationship("StudentProfile", backref="sub_fields")

    def __init__(self, 
    id,
    SF_Id,
    Title,
    description,
    FOS,
    sample_image,
    reg_at,
    reg_by,
    upd_at,
    upd_by):
        
        id=id
        SF_Id=SF_Id
        Title=Title
        description=description
        FOS=FOS
        sample_image=sample_image
        reg_at=reg_at
        reg_by=reg_by
        upd_at=upd_at
        upd_by=upd_by

    def __repr__(self):
        return f"<{self.Title}-----is under ----{self.FOS}-------{self.description}>"

