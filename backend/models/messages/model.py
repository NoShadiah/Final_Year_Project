from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Message(db.Model):
   
    __tablename__ = "messages"

    id: int
    Comm_Id: str
    Sender_Id: str
    message_body: str
    Admin_Id: str
    resp_body:str
    sent_at: str
    responded_at:str

    id = db.Column(db.Integer, unique=True, nullable=False)
    Comm_Id = db.Column(db.String(7), primary_key=True)
    Sender_Id = db.Column(db.String(5), db.ForeignKey("users.U_Id"))
    message_body = db.Column(db.Text, nullable=False)
    Admin_Id = db.Column(db.String(2), db.ForeignKey("admins.A_Id"))
    resp_body = db.Column(db.Text, nullable=True)
    sent_at = db.Column(db.String(30), default=datetime.now())
    responded_at = db.Column(db.String(30), onupdate=datetime.now())