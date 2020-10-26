from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    category = RadioField('Category', choices=[('Interview','Interview'),('Slogan','Slogan'),('Advertisement','Advertisement'),('Pickup-lines','Pickup-lines')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    

class CommentForm(FlaskForm):
    comment = TextAreaField('Comments.',validators = [Required()])
    submit = SubmitField('Submit') 

class Upvote(FlaskForm):
    submit = SubmitField('Like') 

class Downvote(FlaskForm):
    submit = SubmitField('Dislike')             