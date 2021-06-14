import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


@dataclass
class Message(db.Model):
    id: int
    timestamp: dt.datetime
    sender: str
    receiver: str
    content: str
    is_read: bool

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=False)
    sender = db.Column(db.String(50), unique=False)
    receiver = db.Column(db.String(50), unique=False)
    content = db.Column(db.String(10000), unique=False)
    is_read = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self, timestamp, sender, receiver, content):
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.content = content
