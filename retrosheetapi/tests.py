"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.failUnlessEqual(1 + 1, 2)
#
#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.
#
#>>> 1 + 1 == 2
#True
#"""}
#
from retrosheetapi.models.lineup_entry import LineupEntry
class LineupEntryTest(TestCase):
  def test_defensive_position_to_name(self):
    pitcher = LineupEntry.defensive_position_to_name(1)
    self.failUnlessEqual(pitcher, u'P')

    pitcher = LineupEntry.defensive_position_to_name(8)
    self.failUnlessEqual(pitcher, u'CF')

from retrosheetapi.models.lineup import Lineup
class LineupTest(TestCase):
  def test_to_string(self):
    pass
