from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch#, Comment, Upvote, Downvote
from flask_login import login_required, current_user
from .. import db
from .forms import PitchForm, UpdateProfile #, CommentForm, Upvote, Downvote
# Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    interview = Pitch.query.filter_by(category = 'Interview').all() 
    slogan = Pitch.query.filter_by(category = 'Slogan').all()
    advertisements = Pitch.query.filter_by(category = 'Advertisement').all()
    pickup = Pitch.query.filter_by(category = 'Pickup-lines')
    title = 'Home||Pitches'
    return render_template('index.html', title = title, interview = interview, slogan = slogan, advertisements = advertisements, pickup = pickup)

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch_title = form.title.data
        pitch = form.pitch.data
        category = form.category.data

        new_pitch = Pitch(pitch_title = pitch_title, pitch = pitch, category = category)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = 'Pitches// new pitch'
    return render_template('pitches.html',title = title, pitch_form = form)  

# 
# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form = ReviewForm()
#     movie = get_movie(id)
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         # Updated review instance
#         new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)
# # 
# # 
#  
#   


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