from flask import render_template
from . import main
# from .models import pitch
from .forms import PitchForm
# Review = review.Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# @main.route('/pitches', methods = ['GET','POST'])
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