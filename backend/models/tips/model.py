from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Tip(db.Model):
    __tablename__ = "tips"

    id: int
    T_Id: str
    T_title: str
    T_body: str
    source: str
    Post_Date: str
    sample_img: str
    reg_by: str 
    
    id = db.Column(db.Integer, nullable=False, unique=True)
    T_Id = db.Column(db.String(7), primary_key=True)
    T_title = db.Column(db.String(50), nullable=False)
    T_body = db.Column(db.Text, nullable=False, unique=True)
    source = db.Column(db.String(70), nullable=False)
    Post_Date = db.Column(db.String(50), default = datetime.now())
    sample_img = db.Column(db.String(100), nullable=False)
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id")) 