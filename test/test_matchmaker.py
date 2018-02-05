import unittest

from matchmaker import *

class TestPerson(unittest.TestCase):
    def test_id_increments(self):
        person_a = Person()
        person_b = Person()

        self.assertGreater(person_b.id, person_a.id)
