from collections import defaultdict
from unittest import TestCase

from day14_1 import Rule, main, get_required, does_produce, main_using_class
from day14_2 import main_brute_force as main2_brute_force, main_smarter


class TestDay14Quick(TestCase):
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
        self.assertEqual(main(lines)[0], 31)
        with open('data/test14_2.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines)[0], 165)
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines)[0], 13312)
        with open('data/test14_4.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines)[0], 180_697)
        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines)[0], 2_210_736)

    def test_main_part_1_using_class(self):
        with open('data/test14_1.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main_using_class(lines), 31)
        with open('data/test14_2.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main_using_class(lines), 165)
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main_using_class(lines), 13312)
        with open('data/test14_4.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main_using_class(lines), 180_697)
        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main_using_class(lines), 2_210_736)

    def test_main_part_2_brute_force(self):
        # 1 case for v3 passes brute force
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        resources = defaultdict(lambda: 0)
        resources['ORE'] = 13312
        self.assertEqual(main2_brute_force(lines, resources), 1)

        # 2 case for v3 passes brute force
        resources = defaultdict(lambda: 0)
        resources['ORE'] = 13312 * 2
        self.assertEqual(main2_brute_force(lines, resources), 2)

        # max case for v3 ... takes a long time
        # resources = defaultdict(lambda: 0)
        # resources['ORE'] = 1_000_000_000_000
        # self.assertEqual(main2_brute_force(lines, resources), 82_892_753)

        # 1 case for v4 passes
        with open('data/test14_4.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        resources = defaultdict(lambda: 0)
        resources['ORE'] = 180_697
        self.assertEqual(main2_brute_force(lines, resources), 1)

        # max case for v4
        # resources = defaultdict(lambda: 0)  # because resources will get mutated
        # resources['ORE'] = 1_000_000_000_000
        # self.assertEqual(main2(lines, 180697), 5586022)

        # 1 case for v5 passes
        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        resources = defaultdict(lambda: 0)
        resources['ORE'] = 2_210_736
        self.assertEqual(main2_brute_force(lines, resources), 1)

        # max case for v5
        # resources = defaultdict(lambda: 0)  # because resources will get mutated
        # resources['ORE'] = 1_000_000_000_000
        # self.assertEqual(main2(lines, 460664))


class TestDay14Slow(TestCase):
    def test_main_part_2_brute_force(self):
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]

        # max case for v3 smarter...passes in 4.45 hours
        # self.assertEqual(main2_brute_force(lines), 82_892_753)

        # max case for v4...passes in 4.6 hours
        with open('data/test14_4.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        # self.assertEqual(main2_brute_force(lines), 5_586_022)

        with open('data/test14_5.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main2_brute_force(lines), 460_664)

    def test_main_part_2_smarter(self):
        with open('data/test14_3.txt') as f:
            lines = [line.strip() for line in f.readlines()]

        # max case for v3 smarter...unknown
        # this should take about six hours to run
        self.assertEqual(main_smarter(lines), 82_892_753)

        # max case for v4
        # with open('data/test14_4.txt') as f:
        #     lines = [line.strip() for line in f.readlines()]
        #
        # resources = defaultdict(lambda: 0)  # because resources will get mutated
        # resources['ORE'] = 1_000_000_000_000
        # self.assertEqual(main2(lines, 180697), 5586022)

        # max case for v5
        # with open('data/test14_5.txt') as f:
        #     lines = [line.strip() for line in f.readlines()]
        #
        # resources = defaultdict(lambda: 0)  # because resources will get mutated
        # resources['ORE'] = 1_000_000_000_000
        # self.assertEqual(main2(lines, 460664))
