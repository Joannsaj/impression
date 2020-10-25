from flask import render_template
from . import main
# from .models import pitch
from .forms import PitchForm
Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/pitches', methods = ['GET','POST'])
def new_pitch(id):
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = 'Pitches// new pitch'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)    