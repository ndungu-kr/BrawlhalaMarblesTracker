from . import db


# Users Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    brawlhala_id = db.Column(db.Integer, nullable=False)
    brawlhala_name = db.Column(db.String(100), nullable=False)


# Groups Table
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    member_one = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    member_two = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_three = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_four = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_five = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_six = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_seven = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    member_eight = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


# Matches Table
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    second_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    third_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    fourth_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    fifth_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    sixth_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    seventh_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    eighth_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    verified_by = db.Column(db.String, db.ForeignKey('user.brawlhala_id'), nullable=False)


# MarbleHistory Table
class MarbleHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)  
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    defence_matches = db.Column(db.Integer, default=0)

