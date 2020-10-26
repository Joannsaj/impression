import unittest
from app.models import Pitch,User
from app import db
class TestReview(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=2, pitch_title='title', category='slogan', pitch ='This pitch is the best thing since sliced bread',user = self.user_James )
    def tearDown(self):
        Review.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,2)
        self.assertEquals(self.new_pitch.pitch_title,'title')
        self.assertEquals(self.new_pitch.category,'slogan')
        self.assertEquals(self.new_pitch.pitch,'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_James)
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
    
