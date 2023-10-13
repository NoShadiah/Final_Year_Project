from models.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class InterviewQuestion(db.Model):
    __tablename__ = "interview_questions"

    id: int
    Qn_Id: str
    Q_Title: str
    Qn_body: str
    IQC_Id: str
    reg_at: str
    reg_by: str
    upd_at: str
    upd_by: str

    id = db.Column(db.Integer, nullable=False, unique=True)
    Qn_Id = db.Column(db.String(9), primary_key=True)
    Q_Title = db.Column(db.String(70), nullable=True)
    Qn_body = db.Column(db.Text, nullable=True, unique=True)
    IQC_Id = db.Column(db.String(7), db.ForeignKey("question_categories.IQC_ID"))
    reg_at = db.Column(db.String(100), nullable=False, default=datetime.now()) 
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)
    upd_at = db.Column(db.String(100), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"), nullable=False)

    def __init__(self, 
                id,
                Qn_Id,
                Q_Title,
                Qn_body,
                IQC_Id,
                reg_at,
                reg_by,
                upd_at,
                upd_by):

                self.id = id
                self.Qn_Id = Qn_Id
                self.Q_Title = Q_Title
                self.Qn_body = Qn_body
                self.IQC_Id = IQC_Id
                self.reg_at = reg_at
                self.reg_by = reg_by
                self.upd_at = upd_at
                self.upd_by = upd_by

    def __repr__(self):
            return f"<Interview Question{self.Qn_Id}---------{self.Qn_body}>"