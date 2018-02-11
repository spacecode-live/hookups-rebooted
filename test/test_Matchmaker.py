from matchmaker import *

import unittest


class TestMatchmaker(unittest.TestCase):
    def test_init(self):
        m = Matchmaker()
        self.assertEqual(m.queue, [])

    def test_queue_person(self):
        m = Matchmaker()
        p = Person()
        m.queue_person(p)
        self.assertIn(p, m.queue)

    def test_clear_queue(self):
        m = Matchmaker()
        p = Person()
        m.queue_person(p)
        m.clear_queue()
        self.assertEqual(m.queue, [])

    def test_matchmake1(self):
        m = Matchmaker()
        p = Person()
        o = Person()

        p.gender = Gender.female
        p.preference = Gender.female 
        p.interest = Interest.every
        o.gender = Gender.female
        o.preference = Gender.female
        o.interest = Interest.every

        m.queue_person(p)
        self.assertIn(p, m.queue)
        m.queue_person(o)
        self.assertNotIn(p, m.queue)
