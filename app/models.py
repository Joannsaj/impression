from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure  = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    downvote = db.relationship('Downvote',backref = 'user',lazy = "dynamic")
    upvote = db.relationship('Upvote',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
    downvote = db.relationship('Downvote',backref = 'pitch',lazy = "dynamic")
    upvote = db.relationship('Upvote',backref = 'pitch',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.pitch}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()
        return upvotes

    def __repr__(self):
        return f'Upvote {self.upvote}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvotes = Downvote.query.filter_by(pitch_id=id).all()
        return downvotes

    def __repr__(self):
        return f'Downvote {self.downvote}'        

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    commment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f'Comment {self.comment}'           