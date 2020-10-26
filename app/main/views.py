from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch, Comment, Upvote, Downvote
from flask_login import login_required, current_user
from .. import db
from .forms import PitchForm, UpdateProfile , CommentForm#, Upvote, Downvote
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
    return render_template('index.html', title = title, pitches = pitches, interview = interview, slogan = slogan, advertisements = advertisements, pickup = pickup)

def votes():
    pitches = Pitch.query.all()
    likes = Upvote.query.all()
    dislikes = Downvote.query.all()
    user = current_user
    return render_template('index.html', pitches=pitches, likes=likes, user=user, dislikes = dislikes)

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch_title = form.title.data
        pitch = form.pitch.data
        category = form.category.data

        new_pitch = Pitch(pitch_title = pitch_title, pitch = pitch, category = category, user=current_user)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = 'Pitches// new pitch'
    return render_template('pitches.html',title = title, pitch_form = form)  


@main.route('/view_comments/<id>')
@login_required
def view_comments(id):
    comment = Comment.get_comments(id)
    title = "View Comments"
    return render_template('comment.html', comment_list= comment, title=title)

@main.route('/comment/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form= CommentForm()
    pitch = Pitch.query.filter_by(id= pitch_id).first()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, user = current_user, pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('new_comment.html', comment_form= form,pitch_id=pitch_id)


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


@main.route('/like/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def upvote(pitch_id):
    pitches = Pitch.query.get(id )
    like = Upvote( upvote=1)
    like.save_upvote()
    return redirect(url_for('.upvote'))    

@main.route('/dislike/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def downvote(pitch_id):
    pitches = Pitch.query.get(id)
    dislike = Downvote( downvote=1)
    dislike.save_downvote()
    return redirect(url_for('.downvote'))      