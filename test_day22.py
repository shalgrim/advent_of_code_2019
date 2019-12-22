from unittest import TestCase
from day22_1 import shuffle


lines1 = ['deal with increment 7', 'deal into new stack', 'deal into new stack']

lines2 = ['cut 6', 'deal with increment 7', 'deal into new stack']

lines3 = ['deal with increment 7', 'deal with increment 9', 'cut -2']

lines4 = [
    'deal into new stack',
    'cut -2',
    'deal with increment 7',
    'cut 8',
    'cut -4',
    'deal with increment 7',
    'cut 3',
    'deal with increment 9',
    'deal with increment 3',
    'cut -1',
]


class TestDay22(TestCase):
    def test_shuffle(self):
        self.assertEqual(' '.join([str(i) for i in shuffle(lines1, 10)]), '0 3 6 9 2 5 8 1 4 7')
        self.assertEqual(' '.join([str(i) for i in shuffle(lines2, 10)]), '3 0 7 4 1 8 5 2 9 6')
        self.assertEqual(' '.join([str(i) for i in shuffle(lines3, 10)]), '6 3 0 7 4 1 8 5 2 9')
        self.assertEqual(' '.join([str(i) for i in shuffle(lines4, 10)]), '9 2 5 8 1 4 7 0 3 6')
