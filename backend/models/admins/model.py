from models.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Admin(db.Model):
    __tablename__ = 'admins'

    # representation of columns on retrieval
    id: int
    A_Id: str
    F_name: str
    L_name: str
    age: int
    gender: str
    email: str
    Contact: int
    Address: str
    password: str
    Reg_at: str
    updated_at: str

    id = db.Column(db.Integer)
    A_Id = db.Column(db.String(2), primary_key = True, nullable=False)
    F_name: db.Column(db.String(20), nullable=False)
    L_name: db.Column(db.String(20), nullable=False)
    age: db.Column(db.Integer, nullable=False)
    gender: db.Column(db.String(6), nullable=False)
    email: db.Column(db.String(50), nullable=False)
    Contact: db.Column(db.String(10), nullable=False)
    Address: db.Column(db.String(100), nullable=False)
    password: varchar
    Reg_at = db.Column(db.String, nullable=False, default=datetime.now())
    updated_at = db.Column(db.String, nullable=True, default=datetime.now())

    def __init__(self, A_Id, Reg_at):
        pass