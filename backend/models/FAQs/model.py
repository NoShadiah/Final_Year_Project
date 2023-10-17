from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FAQ(db.Model):
    __tablename__= "frequently_asked_questions"

    id: int
    FAQ_Id: str
    U_Id: str
    Qn_body: str
    Post_Date: str
    Resp_by: str
    Resp_Body: str
    updated_at: str

    id =db.Column(db.Integer, nullable=False, unique=False)
    FAQ_Id = db.Column(db.String(5), primary_key=True)
    U_Id = db.Column(db.String(5), db.ForeignKey("users.U_Id"))
    Qn_body = db.Column(db.Text, nullable=False, unique = True)
    Post_Date = db.Column(db.String(30), default=datetime.now)
    Resp_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"))
    Resp_Body = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.String(30), onupdate=datetime.now())