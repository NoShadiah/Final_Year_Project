from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class InterviewQuestionCategory(db.Model):
    __tablename__ = "question_categories"

    id: int
    IQC_ID: str
    QC_name: str
    subfield_Id: str
    Education_level: str
    reg_at: str
    reg_by: str
    upd_at: str
    upd_by: str

    id = db.Column(db.Integer, nullable=False, unique=True)
    IQC_ID = db.Column(db.String(7), nullable=False, primary_key=True)
    QC_name = db.Column(db.String(4), nullable=False, unique=True)
    subfield_Id = db.Column(db.String(6), nullable=False)
    Education_level = db.Column(db.String(20), nullable=False)
    reg_at = db.Column(db.String(100), nullable=False, default=datetime.now()) 
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)
    upd_at = db.Column(db.String(100), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)
    

    def __init__(self,
                id,
                IQC_ID,
                QC_name,
                subfield_Id,
                Education_level,
                reg_at,
                reg_by,
                upd_at,
                upd_by):


                self.id=id
                self.IQC_ID=IQC_ID
                self.QC_name=QC_name
                self.subfield_Id=subfield_Id
                self.Education_level=Education_level
                self.reg_at = reg_at
                reg_by = reg_by
                upd_at = upd_at
                upd_by = upd_by

    def __repr__(self):
            return f"<Question Category -------- {self.QC_name}"