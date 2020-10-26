from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    

class CommentForm(FlaskForm):
    comment = TextAreaField('Comments.',validators = [Required()])
    submit = SubmitField('Submit') 

class Upvote(FlaskForm):
    upvote = TextAreaField('Like',validators = [Required()])
    submit = SubmitField('Submit') 

class Downvote(FlaskForm):
    dislike = TextAreaField('Dislike',validators = [Required()])
    submit = SubmitField('Submit')             