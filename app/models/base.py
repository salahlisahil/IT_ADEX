from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()


class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default='Default title of statistics block')
    count = db.Column(db.Integer, default=0)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    image = db.Column(db.String(255))
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    topic = db.Column(db.String(100))

    def __repr__(self):
        return f'<Category: {self.title}>'


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    image = db.Column(db.String(255))
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    topic = db.Column(db.String(100))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('project_category', lazy=True))

    github = db.Column(db.String(1000))
    behance = db.Column(db.String(1000))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    image = db.Column(db.String(255))
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    facebook = db.Column(db.String(1000))
    twitter = db.Column(db.String(1000))
    dribbble = db.Column(db.String(1000))
    instagram = db.Column(db.String(1000))
    youtube = db.Column(db.String(1000))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    header = db.Column(db.String(100))
    message = db.Column(db.String(1000))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
