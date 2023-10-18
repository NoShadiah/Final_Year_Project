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
    id = db.Column(db.Integer, primary_key = True)
    ur_Id = db.Column(db.String(5), nullable=False, unique=True)
    title = db.Column(db.String(70), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=True)
    reg_at = db.Column(db.String(50), nullable=False, default=datetime.now())
    reg_by = db.Column(db.String(2), db.ForeignKey("admins.A_Id"))
    upd_at = db.Column(db.String(50), nullable=False, onupdate=datetime.now())
    upd_by = db.Column(db.String(2), default="Not yet")

    