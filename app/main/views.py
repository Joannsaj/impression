from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required
from .. import db
from .forms import UpdateProfile
# Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home||Pitches'
    return render_template('index.html', title = title)

# @main.route('/pitches', methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = PitchForm()

#     if form.validate_on_submit():
#         title = form.title.data
#         pitch = form.pitch.data
#         category = form.category,data
#         new_pitch = Pitch(movie.id,title,movie.poster,review)
#         new_review.save_review()
#         return redirect(url_for('movie',id = movie.id ))

#     title = 'Pitches// new pitch'
#     return render_template('pitches.html',title = title, pitch_form = form, movie=movie)    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)