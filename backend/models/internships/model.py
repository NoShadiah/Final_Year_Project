from models.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Internship(db.Model):
    __tablename__ = "internships"

    