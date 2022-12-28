from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        self.assertEqual(calc.add(5, 6), 11)

    def test_subtract_numbers(self):
        self.assertEqual(calc.subtract(10, 15), 5)
