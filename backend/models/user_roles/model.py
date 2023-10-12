from db import db
from datetime import datetime
from dataclasses import dataclass
from models.admins.model import Admin
@dataclass
class UserRole(db.Model):
    __tablename__ = "user_roles"

    id: int
    ur_Id: str
    description: str
    Reg_at: str
    Reg_by: str
    upd_at: str
    upd_by: str

    # columns
    id = db.Column(db.Integer)
    ur_Id = db.Column(db.String(5), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    reg_at = db.Column(db.String, nullable=False, default=datetime.now())
    reg_by = db.Column(db.String(3), db.ForeignKey("admins.A_Id"))
    upd_at = db.Column(db.String, nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(3), db.ForeignKey("admins.A_Id"))

    def __init__(self, ur_id, description,
                 reg_at, reg_by, upd_at, upd_by):
        
