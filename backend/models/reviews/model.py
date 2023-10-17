from datetime import datetime
from dataclasses import dataclass
from models.db import db

@dataclass
class Review(db.Model):
    __tablename__ = "reviews"

    id: int
    R_Id: str
    reviewer_id: str
    review_text: str
    rating: int
    admin_feedback: str
    made_at: str
    upd_at: str

    id = db.Column(db.Integer, unique=True, nullable=False)
    R_Id = db.Column(db.String(6), primary_key = True)
    reviewer_id = db.Column(db.String(5), db.ForeignKey("users.U_Id"))
    review_text = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    admin_feedback = db.Column(db.String(200), nullable=True)
    admin_Id = db.Column(db.String(2), db.ForeignKey("admins.A_Id"))
    made_at = db.Column(db.String(30), default=datetime.now())
    upd_at = db.Column(db.String(30), onupdate=datetime.now())