import unittest

from misc.domain.coordinates import Coordinates
from misc.domain.directions.direction_horizontal import DirectionHorizontal
from misc.domain.directions.direction_vertical import DirectionVertical


class TestCoordinates(unittest.TestCase):
    def setUp(self):
        self.coord1 = Coordinates(0, 0)
        self.coord2 = Coordinates(1, 0)
        self.coord3 = Coordinates(0, 1)
        self.coord4 = Coordinates(1, 1)

    def test_repr(self):
        self.assertEqual(repr(self.coord1), 'Coordinates (0, 0)')

    def test_short_repr(self):
        self.assertEqual(self.coord1.short_repr, '(0, 0)')

    def test_adjacent_to_horizontal(self):
        self.assertIsInstance(self.coord1.adjacent_to(self.coord2), DirectionHorizontal)

    def test_adjacent_to_vertical(self):
        self.assertIsInstance(self.coord1.adjacent_to(self.coord3), DirectionVertical)

    def test_adjacent_to_none(self):
        self.assertIsNone(self.coord1.adjacent_to(self.coord4))

    def test_same_as(self):
        self.assertTrue(self.coord1.same_as(Coordinates(0, 0)))
        self.assertFalse(self.coord1.same_as(self.coord2))

    def test_shifted_coordinates(self):
        shifted = self.coord1.shifted_coordinates(1, 1)
        self.assertEqual(shifted, Coordinates(1, 1))

    def test_neighbouring_coordinates(self):
        neighbours = self.coord1.neighbouring_coordinates
        expected = [(0 - 1, 0), (0 + 1, 0), (0, 0 - 1), (0, 0 + 1)]
        self.assertEqual(neighbours, expected)
