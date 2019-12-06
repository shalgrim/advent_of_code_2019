from unittest import TestCase
from day06_1 import count_all_orbits

TEST_LINES = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""


class TestDay06(TestCase):
    def test_count_all_orbits(self):
        lines = [line.strip() for line in TEST_LINES.split('\n') if line]
        self.assertEqual(42, count_all_orbits(lines))
