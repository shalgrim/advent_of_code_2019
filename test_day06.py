from unittest import TestCase
from day06_1 import count_all_orbits
from day06_2 import me_to_santa_count

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

TEST_LINES_2 = """COM)B
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
K)YOU
I)SAN
"""


class TestDay06(TestCase):
    def test_count_all_orbits(self):
        lines = [line.strip() for line in TEST_LINES.split('\n') if line]
        self.assertEqual(42, count_all_orbits(lines))

    def test_me_to_santa_count(self):
        lines = [line.strip() for line in TEST_LINES_2.split('\n') if line]
        self.assertEqual(4, me_to_santa_count(lines))
