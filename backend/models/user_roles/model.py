from models.db import db
from datetime import datetime
from dataclasses import dataclass
from models.admins.model import Admin
@dataclass
class UserRole(db.Model):
    __tablename__ = "user_roles"

    id: int
    ur_Id: str
    title: str
    description: str
    reg_at: str
    reg_by: str
    upd_at: str
    upd_by: str

    # columns
    id = db.Column(db.Integer, nullable = False, unique=True)
    ur_Id = db.Column(db.String(5), nullable=False, unique=True, primary_key = True)
    title = db.Column(db.String(70), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=True)
    reg_at = db.Column(db.String(50), nullable=False, default=datetime.now())
    reg_by = db.Column(db.String(3), db.ForeignKey("admins.A_Id"))
    upd_at = db.Column(db.String(50), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(3), db.ForeignKey("admins.A_Id"))

    def __init__(self, ur_id, description,title,
                 reg_at, reg_by, upd_at, upd_by):
        self.ur_id = ur_id
        self.title = title
        self.description = description
        self.reg_at = reg_at
        self.reg_by= reg_by
        self.upd_at = upd_at
        self.upd_by = upd_by

    def __repr__(self):
        return f"<{self.title} :{self.description}>"