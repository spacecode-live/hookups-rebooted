import unittest

from matchmaker import *

class TestPerson(unittest.TestCase):
    def test_id_increments(self):
        person_a = Person()
        person_b = Person()
        self.assertGreater(person_b.id, person_a.id)


    def test_is_interested_in(self):
        person_a = Person()
        person_b = Person()

        person_a.gender = Gender.female
        person_a.preference = Gender.female
        person_b.gender = Gender.female
        person_b.preference = Gender.female
        person_a.interest = Interest.kiss
        person_b.interest = Interest.kiss
        self.assertTrue(person_a.is_interested_in(person_b))

        person_a.gender = Gender.male
        person_a.preference = Gender.female
        person_b.gender = Gender.female
        person_b.preference = Gender.male
        person_a.interest = Interest.every
        person_b.interest = Interest.romance
        self.assertTrue(person_a.is_interested_in(person_b))

        person_a.gender = Gender.male
        person_a.preference = Gender.female
        person_b.gender = Gender.male
        person_b.preference = Gender.male
        person_a.interest = Interest.every
        person_b.interest = Interest.every
        self.assertFalse(person_a.is_interested_in(person_b))
