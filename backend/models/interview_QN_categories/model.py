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
    upd_by = db.Column(db.String(2), default="Not yet")

    interview_questions = db.relationship("InterviewQuestion", backref="question_category", lazy="dynamic")
    

    