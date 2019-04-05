from django.test import TestCase

from .models import Profile,Project,Votes
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kayitare= Profile(name="kayitare",picture="insto/pexels-photo-1464216.jpeg",bio="<p>sghjjrt</p>")
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kayitare,Profile))
        # Testing Save Method
    def test_save_method(self):
        self.kayitare.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

# Create your tests here.
