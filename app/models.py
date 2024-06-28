from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    brawlhala_id = db.Column(db.Integer, nullable=True)
    brawlhala_name = db.Column(db.String(100), nullable=True)
    groups = db.relationship('GroupMember', backref="user", lazy=True)
    matches = db.relationship('MatchParticipant', backref="user", lazy=True)
    marbles = db.relationship('MarbleHistory', backref="user", lazy=True)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    members = db.relationship('GroupMember', backref="group", lazy=True)
    matches = db.relationship('Match', backref="group", lazy=True)
    marbles = db.relationship('MarbleHistory', backref="group", lazy=True)


class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    verified_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class MatchParticipant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)  # 1 for winner, 2 for second, etc.


class MarbleHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    defence_matches = db.Column(db.Integer, default=0)

    