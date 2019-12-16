from unittest import TestCase

from day14_1 import Rule, main, get_required, does_produce
from day14_2 import main as main2


class TestDay14(TestCase):
    def test_does_produce(self):
        with open('data/test14_1.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        rules = [Rule(line) for line in lines]
        rules = {rule.output: rule for rule in rules}
        self.assertFalse(does_produce('A', 'ORE', rules))
        self.assertFalse(does_produce('B', 'ORE', rules))
        self.assertFalse(does_produce('C', 'ORE', rules))
        self.assertFalse(does_produce('D', 'ORE', rules))
        self.assertFalse(does_produce('E', 'ORE', rules))
        self.assertFalse(does_produce('FUEL', 'ORE', rules))
        self.assertTrue(does_produce('ORE', 'A', rules))
        self.assertTrue(does_produce('ORE', 'B', rules))
        self.assertTrue(does_produce('ORE', 'C', rules))
        self.assertTrue(does_produce('ORE', 'D', rules))
        self.assertTrue(does_produce('ORE', 'E', rules))
        self.assertTrue(does_produce('ORE', 'FUEL', rules))
        self.assertFalse(does_produce('A', 'B', rules))
        self.assertFalse(does_produce('B', 'A', rules))
        self.assertTrue(does_produce('A', 'C', rules))
        self.assertTrue(does_produce('A', 'D', rules))
        self.assertTrue(does_produce('A', 'E', rules))
        self.assertTrue(does_produce('A', 'FUEL', rules))
        self.assertFalse(does_produce('C', 'A', rules))
        self.assertFalse(does_produce('D', 'A', rules))
        self.assertFalse(does_produce('E', 'A', rules))
        self.assertFalse(does_produce('FUEL', 'A', rules))
        self.assertTrue(does_produce('B', 'C', rules))
        self.assertFalse(does_produce('C', 'B', rules))
        self.assertTrue(does_produce('B', 'D', rules))
        self.assertTrue(does_produce('B', 'E', rules))
        self.assertTrue(does_produce('B', 'FUEL', rules))

    def test_main_part_1(self):
        with open('data/test14_1.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 31)
        with open('data/test14_2.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 165)
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 13312)
        with open('data/test14_4.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 180697)
        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 2210736)

    def test_main_part_2(self):
        # with open('data/test14_3.txt') as f:
        #     lines = [line.strip() for line in f.readlines()]
        # self.assertEqual(main2(lines, 13312), 82892753)
        # with open('data/test14_4.txt') as f:
        #     lines = [line.strip() for line in f.readlines()]
        # self.assertEqual(main2(lines, 180697), 5586022)
        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main2(lines), 460664)  # returned 460663 =(
