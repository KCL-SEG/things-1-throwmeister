from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Thing

class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing : Thing = Thing(
            name='alex',
            description='alex takes things',
            quantity=4
        )
    
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail("Test user should be valid")
    
    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
    
    def test_testing(self):
        self._assert_thing_is_valid()
    
    