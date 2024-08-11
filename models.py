from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SearchLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
